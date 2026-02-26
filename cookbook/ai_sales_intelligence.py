#!/usr/bin/env python3
"""
AI Sales Intelligence — Replace your CRM with a Knowledge Graph

This cookbook shows how to build an AI-powered sales intelligence system using
Papr Memory's schema builder DSL. Instead of manually updating Attio/HubSpot/
Salesforce, you feed in conversations and the engine auto-extracts companies,
contacts, deals, intents, and competitive signals — all type-enforced.

Use-cases covered:
  1. Auto-CRM from conversations (calls, emails, Slack)
  2. Deal risk assessment (AI-assessed from conversation tone)
  3. Intent signal detection (controlled vocabulary, no hallucination)
  4. Pipeline stage tracking (auto-detect stage transitions)
  5. Competitive intelligence (track competitor mentions)
  6. Relationship strength (auto-assess from interaction patterns)
  7. Action item extraction (pull next steps from every interaction)

Attio field mapping:
  - Company (34 Attio attrs) → Company node (10 props) + edges + AI fields
  - People (32 Attio attrs)  → Contact node (10 props) + edges + AI fields
  - Deals (14 Attio attrs)   → Deal node (10 props) + edges + AI fields
  - NEW: Interaction, Intent, Stage, Competitor nodes (not in Attio)

  System fields (Record ID, Created at, Created by) → handled by Papr
  Relationship fields (Team, Associated deals/company) → edges
  Interaction tracking (first/last/next) → computed from graph

Prerequisites:
  pip install 'papr_memory>=2.21.0'
  export PAPR_MEMORY_API_KEY="your-api-key"  # from dashboard.papr.ai

Run:
  python cookbook/ai_sales_intelligence.py
"""

import os
import json
import argparse
from typing import Optional, List
from papr_memory import Papr
from papr_memory.lib import (
    schema, node, lookup, upsert, constraint,
    prop, edge, exact, semantic, fuzzy, Auto,
    And, Or, Not,
    build_schema_params, build_link_to, build_memory_policy, serialize_set_values,
)
from papr_memory.types import (
    AddMemoryParam,
    MemoryAddBatchParams,
    BatchMemoryResponse,
)

# ---------------------------------------------------------------------------
# 1. DEFINE THE SCHEMA
# ---------------------------------------------------------------------------
# This is the declarative "write layer" — you define the structure once,
# and the engine enforces it on every memory you add.
#
# Limits: max 10 node types, max 20 relationships, max 10 properties per node.

@schema("ai_sales_platform")
class SalesIntelligence:
    """
    AI Sales Intelligence schema — replaces Attio/HubSpot as system of record.

    7 node types, 9 relationships. The engine auto-extracts entities from
    unstructured text (call transcripts, emails, Slack) and builds a
    knowledge graph you can query via GraphQL.
    """

    # ------------------------------------------------------------------
    # COMPANY — maps to Attio "Companies" object (34 attributes)
    #
    # Attio fields mapped:
    #   domain       ← Domains (unique identifier)
    #   name         ← Name
    #   description  ← Description
    #   categories   ← Categories (multi-select → array)
    #   location     ← Primary location
    #   linkedin     ← LinkedIn
    #   estimated_arr ← Estimated ARR (select)
    #   employee_range ← Employee range (select)
    #   funding_raised ← Funding raised (currency)
    #   deal_risk    ← NEW: AI-assessed from conversations
    #
    # Attio fields → edges:
    #   Team         → Contact.works_at (edge)
    #   Associated deals → Deal.deal_with (edge)
    #
    # Attio fields → computed from graph:
    #   First/Last/Next calendar/email/interaction → query Interaction edges
    #   Connection strength → computed from Contact edges
    #   Strongest connection → computed from Contact edges
    #   Twitter follower count → enrichment (future)
    #
    # Attio system fields (auto-handled by Papr):
    #   Record ID, Created at, Created by, List entries
    # ------------------------------------------------------------------
    @node
    @upsert
    @constraint(
        set={
            "deal_risk": Auto("Assess deal risk from conversation context, "
                              "competitor mentions, and objection patterns. "
                              "Consider: ghosting, pricing pushback, "
                              "competitor evaluation, champion loss."),
        },
    )
    class Company:
        """Company/account — maps to Attio Companies object."""
        domain: str = prop(
            required=True, search=exact(),
            description="Company domain, unique identifier (e.g. 'acme.com'). "
                        "Maps to Attio 'Domains'. Required for Company creation.")
        name: str = prop(
            required=True, search=semantic(0.90),
            description="Company name (e.g. 'Acme Corp'). MUST be an actual "
                        "company or organization name. Do NOT use UUIDs, IDs, "
                        "generic descriptions ('enterprise customer', 'prospect "
                        "company'), or partial identifiers. If you cannot determine "
                        "the company name, do NOT create this Company node. "
                        "Maps to Attio 'Name'.")
        description: str = prop(
            description="What the company does, 1-2 sentences. "
                        "Maps to Attio 'Description'.")
        categories: list = prop(
            type="array",
            description="Industry categories as a list "
                        "(e.g. ['B2B', 'SaaS', 'Enterprise']). "
                        "Maps to Attio 'Categories' (multi-select).")
        location: str = prop(
            description="Primary location (e.g. 'San Francisco, CA'). "
                        "Maps to Attio 'Primary location'.")
        linkedin: str = prop(
            description="LinkedIn company URL. Maps to Attio 'LinkedIn'.")
        estimated_arr: str = prop(
            enum_values=["<1M", "1M-5M", "5M-25M", "25M-100M", "100M+"],
            description="Estimated annual recurring revenue bracket. "
                        "Maps to Attio 'Estimated ARR'.")
        employee_range: str = prop(
            enum_values=["1-10", "11-50", "51-200", "201-1000", "1000+"],
            description="Company size bracket. Maps to Attio 'Employee range'.")
        funding_raised: str = prop(
            description="Total funding raised (e.g. '$25M'). "
                        "Maps to Attio 'Funding raised'.")
        deal_risk: str = prop(
            enum_values=["low", "medium", "high", "critical"],
            description="AI-assessed deal risk level. NEW — not in Attio.")

    # ------------------------------------------------------------------
    # CONTACT — maps to Attio "People" object (32 attributes)
    #
    # Attio fields mapped:
    #   email        ← Email addresses (unique identifier)
    #   name         ← Name (personal name)
    #   description  ← Description
    #   title        ← Job title
    #   phone        ← Phone numbers
    #   location     ← Primary location
    #   linkedin     ← LinkedIn
    #   twitter      ← Twitter
    #   role         ← NEW: AI-assessed buying role
    #   connection_strength ← Connection strength (select, AI-enhanced)
    #
    # Attio fields → edges:
    #   Company      → works_at (edge)
    #   Associated deals → involves (edge)
    #   Associated users → (internal, not modeled)
    #
    # Attio fields → computed from graph:
    #   First/Last/Next calendar/email/interaction → query Interaction edges
    #   Strongest connection → computed from interaction frequency
    #   Twitter follower count → enrichment (future)
    #
    # Attio system fields (auto-handled by Papr):
    #   Record ID, Created at, Created by, List entries, Avatar URL
    # ------------------------------------------------------------------
    @node
    @upsert
    @constraint(
        set={
            "connection_strength": Auto(
                "Assess relationship strength based on interaction "
                "frequency, responsiveness, and tone. Consider: "
                "how often they respond, meeting attendance, "
                "whether they champion your solution internally."),
            "role": Auto(
                "Determine this person's role in the buying process "
                "based on their title, behavior, and how they're "
                "referenced in conversations."),
        },
    )
    class Contact:
        """Person/contact — maps to Attio People object."""
        email: str = prop(
            required=True, search=exact(),
            description="Primary email address, unique identifier. "
                        "Maps to Attio 'Email addresses'. Required for Contact "
                        "creation — do NOT create a Contact without an email.")
        name: str = prop(
            required=True, search=semantic(0.85),
            description="Full personal name (first AND last name, e.g. 'Sarah Chen'). "
                        "MUST be an actual person's name. Do NOT use job titles "
                        "(CTO, VP, Engineer), pronouns, generic labels (prospect, "
                        "customer, user), or single names. If you cannot determine "
                        "the person's full name, do NOT create this Contact node. "
                        "Maps to Attio 'Name'.")
        description: str = prop(
            description="Notes about this person. Maps to Attio 'Description'.")
        title: str = prop(
            description="Job title (e.g. 'VP Engineering'). "
                        "Maps to Attio 'Job title'. This is separate from name — "
                        "never put a job title in the name field.")
        phone: str = prop(
            description="Phone number. Maps to Attio 'Phone numbers'.")
        location: str = prop(
            description="Primary location (e.g. 'New York, NY'). "
                        "Maps to Attio 'Primary location'.")
        linkedin: str = prop(
            description="LinkedIn profile URL. Maps to Attio 'LinkedIn'.")
        twitter: str = prop(
            description="Twitter/X handle. Maps to Attio 'Twitter'.")
        role: str = prop(
            enum_values=["champion", "decision_maker", "influencer",
                         "end_user", "blocker", "unknown"],
            description="AI-assessed role in the buying process. "
                        "NEW — not in Attio.")
        connection_strength: str = prop(
            enum_values=["very_strong", "strong", "good", "weak",
                         "very_weak", "no_communication"],
            description="AI-assessed relationship strength. "
                        "Maps to Attio 'Connection strength'.")

    # ------------------------------------------------------------------
    # DEAL — maps to Attio "Deals" object (14 attributes)
    #
    # Attio fields mapped:
    #   name         ← Deal name (required)
    #   stage        ← Deal stage (status, required)
    #   owner        ← Deal owner (user, required)
    #   value        ← Deal value (currency)
    #   source       ← Source (select)
    #   loss_reason  ← Loss reason (select)
    #   win_reason   ← Win reason (select)
    #   deal_risk    ← NEW: AI-assessed
    #   win_probability ← NEW: AI-assessed
    #   next_task    ← Next due task (text summary)
    #
    # Attio fields → edges:
    #   Associated people  → involves (edge)
    #   Associated company → deal_with (edge)
    #
    # Attio system fields (auto-handled by Papr):
    #   Record ID, Created at, Created by, List entries
    # ------------------------------------------------------------------
    @node
    @upsert
    @constraint(
        set={
            "name": Auto(
                "Generate a deal name in the format '{Company} - {Context}' "
                "where {Company} is the company name and {Context} is the "
                "product or use-case being discussed (e.g. 'Acme Corp - ML Platform', "
                "'Luminary AI - Agent Memory'). Use the same name across all "
                "conversations about the same opportunity at the same company. "
                "If there is only one deal with a company, a simple "
                "'{Company} - Deal' is acceptable."),
            "deal_risk": Auto("Assess deal risk considering: competitor "
                              "mentions, pricing objections, timeline delays, "
                              "champion availability, budget concerns."),
            "win_probability": Auto("Estimate win probability as a percentage "
                                    "based on deal signals, stage, and risk."),
        },
    )
    class Deal:
        """Deal/opportunity — maps to Attio Deals object."""
        name: str = prop(
            required=True, search=semantic(0.80),
            description="Deal name in '{Company} - {Context}' format "
                        "(e.g. 'Acme Corp - ML Platform'). MUST include the "
                        "company name so deals can be matched across conversations. "
                        "Maps to Attio 'Deal name'.")
        stage: str = prop(
            enum_values=["lead", "qualified", "discovery", "testing",
                         "proposal_contract", "won", "lost"],
            description="Current pipeline stage. "
                        "Maps to Attio 'Deal stage'.")
        owner: str = prop(
            description="Deal owner name (e.g. 'Shawkat Kabbara'). "
                        "Maps to Attio 'Deal owner'.")
        value: str = prop(
            description="Deal value in USD (e.g. '$100,000'). "
                        "Maps to Attio 'Deal value'.")
        source: str = prop(
            enum_values=["inbound", "outbound", "referral", "partner",
                         "event", "other"],
            description="Lead source. Maps to Attio 'Source'.")
        loss_reason: str = prop(
            enum_values=["pricing", "competitor", "timing", "no_budget",
                         "no_champion", "feature_gap", "went_dark", "other"],
            description="Why the deal was lost. Maps to Attio 'Loss reason'.")
        win_reason: str = prop(
            enum_values=["product_fit", "pricing", "relationship",
                         "speed", "integration", "other"],
            description="Why the deal was won. Maps to Attio 'Win reason'.")
        deal_risk: str = prop(
            enum_values=["low", "medium", "high", "critical"],
            description="AI-assessed deal risk. NEW — not in Attio.")
        win_probability: str = prop(
            description="AI-estimated win probability (e.g. '68%'). "
                        "NEW — not in Attio.")
        next_task: str = prop(
            description="Next due task/action item. "
                        "Maps to Attio 'Next due task'.")

    # ------------------------------------------------------------------
    # INTERACTION — NEW (not in Attio)
    #
    # Attio tracks interaction timestamps on Company/People but doesn't
    # store the actual content. This node is the core ingestion point —
    # every call, email, meeting, Slack message becomes an Interaction
    # that the engine uses to auto-update all other nodes.
    # ------------------------------------------------------------------
    @node
    @upsert
    @constraint(
        set={
            "summary": Auto("Summarize this interaction in 1-2 sentences, "
                            "focusing on key decisions, objections raised, "
                            "and next steps agreed upon."),
            "action_items": Auto("Extract action items as a comma-separated "
                                 "list (e.g. 'Send proposal by Friday, "
                                 "Schedule technical deep-dive')."),
            "sentiment": Auto("Assess overall sentiment of the interaction."),
        },
    )
    class Interaction:
        """Interaction — call transcript, email, meeting, Slack message.
        NEW: Attio only tracks timestamps, not content."""
        summary: str = prop(
            required=True, search=semantic(0.85),
            description="AI-generated interaction summary, 1-2 sentences.")
        type: str = prop(
            enum_values=["call", "email", "meeting", "slack", "chat", "other"],
            description="Interaction channel.")
        sentiment: str = prop(
            enum_values=["very_positive", "positive", "neutral",
                         "negative", "very_negative"],
            description="AI-assessed interaction sentiment.")
        action_items: str = prop(
            description="Comma-separated action items extracted from interaction.")
        date: str = prop(
            type="datetime",
            description="When the interaction occurred (ISO 8601).")
        participants: list = prop(
            type="array",
            description="List of participant names "
                        "(e.g. ['Sarah Chen', 'James Liu']).")
        channel: str = prop(
            description="Specific channel details "
                        "(e.g. 'Zoom', 'Gmail', '#sales-team').")

    # ------------------------------------------------------------------
    # INTENT — NEW: controlled vocabulary (@lookup, never hallucinate)
    #
    # These are pre-defined buyer signals. The engine matches to existing
    # intents but never creates new ones — preventing graph pollution.
    # This is what makes it better than Attio: automatic intent detection.
    # ------------------------------------------------------------------
    @node
    @lookup
    class Intent:
        """Buyer intent signal — controlled vocabulary, never hallucinated.
        NEW: not in Attio."""
        name: str = prop(
            required=True, search=semantic(0.90),
            description="Intent name (e.g. 'pricing_inquiry').")
        category: str = prop(
            enum_values=["buying_signal", "risk_signal", "neutral"],
            description="Signal category.")

    # ------------------------------------------------------------------
    # STAGE — controlled vocabulary (@lookup, never hallucinate)
    # Maps exactly to Attio pipeline stages.
    # ------------------------------------------------------------------
    @node
    @lookup
    class Stage:
        """Pipeline stage — controlled vocabulary matching Attio pipeline.
        Maps to Attio 'Deal stage' values."""
        name: str = prop(
            required=True, search=semantic(0.85),
            description="Stage name (e.g. 'discovery').")

    # ------------------------------------------------------------------
    # COMPETITOR — NEW: tracks competitive mentions
    # ------------------------------------------------------------------
    @node
    @upsert
    class Competitor:
        """Competitor mentioned in conversations. NEW: not in Attio."""
        name: str = prop(
            required=True, search=semantic(0.85),
            description="Competitor name (e.g. 'Datadog').")
        domain: str = prop(
            search=exact(),
            description="Competitor domain if known (e.g. 'datadog.com').")

    # ------------------------------------------------------------------
    # EDGES — relationships between nodes
    #
    # Replaces Attio relationship fields:
    #   Company.Team → works_at (reverse)
    #   Company.Associated deals → deal_with (reverse)
    #   Deal.Associated people → involves
    #   Deal.Associated company → deal_with
    #   Contact.Company → works_at
    #   Contact.Associated deals → involves (reverse)
    # ------------------------------------------------------------------

    # Contact works at Company (Attio: People.Company relationship)
    works_at = edge(Contact, Company, create="upsert",
                    description="Contact is employed at Company")

    # Deal is with Company (Attio: Deals.Associated company)
    deal_with = edge(Deal, Company, create="upsert",
                     description="Deal is associated with Company")

    # Deal involves Contact (Attio: Deals.Associated people)
    involves = edge(Deal, Contact, create="upsert",
                    description="Contact is involved in Deal")

    # Interaction is with Contact
    with_contact = edge(Interaction, Contact, create="upsert",
                        description="Interaction involved this Contact")

    # Interaction is about a Deal
    about_deal = edge(Interaction, Deal, create="upsert",
                      description="Interaction relates to this Deal")

    # Interaction is about a Company
    about_company = edge(Interaction, Company, create="upsert",
                         description="Interaction mentions this Company")

    # Interaction shows buyer Intent (lookup — controlled vocab)
    shows_intent = edge(
        Interaction, Intent,
        search=(Intent.name.semantic(0.90),),
        create="lookup",
        description="Interaction reveals this buyer intent signal",
    )

    # Interaction at pipeline Stage (lookup — controlled vocab)
    at_stage = edge(
        Interaction, Stage,
        search=(Stage.name.semantic(0.85),),
        create="lookup",
        description="Interaction indicates deal is at this stage",
    )

    # Interaction mentions a Competitor
    mentions_competitor = edge(
        Interaction, Competitor, create="upsert",
        description="Interaction mentions this Competitor",
    )


# ---------------------------------------------------------------------------
# 2. REGISTER THE SCHEMA
# ---------------------------------------------------------------------------

def register_schema(client: Papr, namespace_id: Optional[str] = None):
    """Register the AI Sales Intelligence schema in Papr Memory."""
    params = build_schema_params(SalesIntelligence)

    # Add namespace scoping if provided
    if namespace_id:
        params["namespace_id"] = namespace_id
        params["scope"] = "namespace"

    # Set to active immediately
    params["status"] = "active"
    params["description"] = (
        "AI Sales Intelligence — auto-extracts companies, contacts, deals, "
        "intents, and competitive signals from conversations. Replaces "
        "manual CRM data entry with declarative, policy-driven memory."
    )

    print("Registering schema 'ai_sales_platform'...")
    print(f"  Node types: {list(params.get('node_types', {}).keys())}")
    print(f"  Relationships: {list(params.get('relationship_types', {}).keys())}")
    if namespace_id:
        print(f"  Namespace: {namespace_id}")

    response = client.schemas.create(**params)
    print(f"  Schema created: {response}")
    return response


# ---------------------------------------------------------------------------
# 3. SEED CONTROLLED VOCABULARY
# ---------------------------------------------------------------------------
# Intent and Stage are @lookup nodes — they must exist before the engine
# can link to them. Seed them once.

INTENTS = [
    ("pricing_inquiry", "buying_signal",
     "Prospect asked about pricing, plans, or discounts"),
    ("technical_evaluation", "buying_signal",
     "Prospect is evaluating technical capabilities or running a POC"),
    ("competitor_comparison", "risk_signal",
     "Prospect mentioned comparing with a competitor"),
    ("budget_discussion", "buying_signal",
     "Prospect discussed budget, procurement, or purchasing process"),
    ("timeline_discussion", "buying_signal",
     "Prospect discussed implementation timeline or go-live date"),
    ("stakeholder_alignment", "buying_signal",
     "Prospect mentioned needing buy-in from other stakeholders"),
    ("objection_raised", "risk_signal",
     "Prospect raised a concern, objection, or blocker"),
    ("champion_identified", "buying_signal",
     "Identified an internal champion advocating for the solution"),
    ("going_dark", "risk_signal",
     "Prospect stopped responding or cancelled meetings"),
    ("expansion_interest", "buying_signal",
     "Existing customer expressed interest in expanding usage"),
    ("renewal_risk", "risk_signal",
     "Signals of potential churn or non-renewal"),
    ("referral_given", "buying_signal",
     "Prospect or customer referred another potential buyer"),
]

STAGES = [
    "lead", "qualified", "discovery", "testing",
    "proposal_contract", "won", "lost",
]


def seed_intents_and_stages(client: Papr, namespace_id: Optional[str] = None):
    """Seed controlled vocabulary nodes (Intent, Stage) via a single add_batch call."""
    print("\nSeeding controlled vocabulary...")

    seed_memories: List[AddMemoryParam] = [
        AddMemoryParam(
            content=f"Sales intent signal: {intent_name} ({category}). {description}",
            link_to=build_link_to(SalesIntelligence.Intent.name.exact(intent_name)),
            type="text",
        )
        for intent_name, category, description in INTENTS
    ] + [
        AddMemoryParam(
            content=f"Pipeline stage: {stage_name}",
            link_to=build_link_to(SalesIntelligence.Stage.name.exact(stage_name)),
            type="text",
        )
        for stage_name in STAGES
    ]

    seed_params: MemoryAddBatchParams = {"memories": seed_memories}
    if namespace_id:
        seed_params["namespace_id"] = namespace_id

    seed_response: BatchMemoryResponse = client.memory.add_batch(**seed_params)
    print(f"  Seeded {len(INTENTS)} intents + {len(STAGES)} stages in one batch")
    print(f"  Status: {seed_response.status}  "
          f"successful: {seed_response.total_successful}  "
          f"failed: {seed_response.total_failed}")


# ---------------------------------------------------------------------------
# 4. EXAMPLE: FEED CONVERSATIONS
# ---------------------------------------------------------------------------
# This is the magic — just pass unstructured text and the engine does the rest.
# No parsing code. No CRUD endpoints. The schema IS the pipeline.

# Each item is a typed AddMemoryParam so add_batch gets properly structured input.
# source_type lives in metadata.custom_metadata — the SDK's MemoryType ("text" |
# "code_snippet" | "document") describes the content format, not the channel.
SAMPLE_CONVERSATIONS: list[AddMemoryParam] = [
    # Call transcript — auto-extracts Company, Contact, Deal, Intent, Stage
    AddMemoryParam(
        content=(
            "Call with Sarah Chen (VP Engineering, sarah.chen@acme.com) at "
            "Acme Corp (acme.com). They're based in San Francisco. "
            "Sarah is evaluating our platform for their ML pipeline. Deal value "
            "around $100K. She asked about pricing tiers and mentioned they're "
            "also looking at Datadog for observability. Timeline is Q2 for "
            "decision. She wants a technical deep-dive next week. "
            "Acme is a B2B SaaS company, ~200 employees, Series B ($25M raised)."
        ),
        type="text",
        metadata={"custom_metadata": {"source_type": "call"}},
    ),

    # Email — auto-links to existing nodes, updates deal risk
    AddMemoryParam(
        content=(
            "Email from sarah.chen@acme.com: 'Hi Shawkat, I shared your proposal "
            "with our CTO James Liu (james.liu@acme.com). He's concerned about "
            "the integration timeline with our existing Kubernetes setup. Can we "
            "schedule a call to address his questions? Also, Datadog offered us "
            "a 30% discount. I'm still pushing for your solution internally.'"
        ),
        type="text",
        metadata={"custom_metadata": {"source_type": "email"}},
    ),

    # Slack message — competitive intelligence signal
    AddMemoryParam(
        content=(
            "Internal note: Heard from Sarah that Acme's CTO had a call with "
            "MongoDB Atlas team last week. They're evaluating managed database "
            "solutions too. We need to position our solution's graph capabilities "
            "vs their document model. Risk level increasing — need to get our "
            "champion (Sarah) to set up a meeting with CTO directly."
        ),
        type="text",
        metadata={"custom_metadata": {"source_type": "slack"}},
    ),

    # Meeting notes — stage transition + action items
    AddMemoryParam(
        content=(
            "Technical deep-dive with Acme Corp. Attendees: Sarah Chen, "
            "James Liu (CTO), Priya Patel (Staff Engineer, priya@acme.com). "
            "Demoed the knowledge graph integration. James was impressed by "
            "the GraphQL query layer but wants to see latency benchmarks under "
            "load. Priya will run a POC next sprint. Moving to testing stage. "
            "Action items: Send latency benchmark report, Set up sandbox "
            "environment for Priya, Follow up on security compliance docs."
        ),
        type="text",
        metadata={"custom_metadata": {"source_type": "meeting"}},
    ),

    # New deal — AI startup evaluating Papr for their memory layer
    AddMemoryParam(
        content=(
            "Intro call with Maya Goldberg (Co-founder & CEO, maya@luminary.ai) "
            "at Luminary AI (luminary.ai). They're an early-stage AI startup "
            "based in New York building autonomous research agents. "
            "Categories: B2B, AI Infrastructure, Developer Tools. "
            "Maya wants to replace their hand-rolled vector store with Papr's "
            "knowledge graph to give their agents persistent, queryable memory. "
            "Potential deal worth $48K/year. Maya is the decision maker and very "
            "bought in — moving straight to technical evaluation stage. "
            "Luminary AI has 12 engineers, Seed-funded ($4M)."
        ),
        type="text",
        metadata={"custom_metadata": {"source_type": "call"}},
    ),
]


def feed_conversations(client: Papr, namespace_id: Optional[str] = None) -> None:
    """Feed all sample conversations into Papr Memory in a single batch call."""
    print(f"\nFeeding {len(SAMPLE_CONVERSATIONS)} conversations as a batch...")

    # Build a typed batch params dict for documentation clarity, then unpack it.
    # Schema policies handle everything automatically per memory:
    # - Entity extraction (Company, Contact, Deal, Interaction nodes)
    # - Intent detection (links to existing @lookup Intents)
    # - Stage detection (links to existing @lookup Stages)
    # - Competitor tracking (creates/updates Competitor nodes)
    # - Risk assessment (Auto() constraints fire on relevant nodes)
    # - Summary + action items (Auto() on Interaction node)
    # - Connection strength (Auto() on Contact node)
    # - Role detection (Auto() on Contact node)
    batch_params: MemoryAddBatchParams = {
        "memories": SAMPLE_CONVERSATIONS,
        "external_user_id": "test@papr.ai",
    }
    if namespace_id:
        batch_params["namespace_id"] = namespace_id

    response: BatchMemoryResponse = client.memory.add_batch(**batch_params)

    print(f"  Status      : {response.status}")
    print(f"  Processed   : {response.total_processed}")
    print(f"  Successful  : {response.total_successful}")
    print(f"  Failed      : {response.total_failed}")
    if response.errors:
        for err in response.errors:
            print(f"  [index {err.index}] {err.error}")
    if response.successful:
        for mem in response.successful:
            # Each AddMemoryResponse.data holds the created AddMemoryItem(s)
            ids = [item.memory_id for item in (mem.data or [])]
            print(f"    memory_ids: {ids}  status: {mem.status}")


# ---------------------------------------------------------------------------
# 5. EXAMPLE: TARGETED UPDATES WITH link_to
# ---------------------------------------------------------------------------

def targeted_updates(client: Papr, namespace_id: Optional[str] = None):
    """Show how to use link_to for precise node targeting."""
    print("\nTargeted updates with link_to...")

    base_kwargs = {}
    if namespace_id:
        base_kwargs["namespace_id"] = namespace_id

    # Update a specific deal — pin to exact company domain + contacts
    # NOTE: Be explicit with names in content to avoid garbage nodes.
    # "CTO" alone → engine creates Contact(name="CTO"). Always use full names.
    # "existing enterprise customer" → engine creates Company with that label.
    client.memory.add(
        content=(
            "Acme Corp deal update: Sarah Chen confirmed budget approval but "
            "James Liu (CTO) wants one more reference call before signing. "
            "Moving to proposal stage. Win probability looking good at ~70%. "
            "Next task: arrange reference call with a current customer."
        ),
        link_to=build_link_to(
            SalesIntelligence.Company.domain.exact("acme.com"),
            SalesIntelligence.Deal.name,  # semantic match on deal name
            SalesIntelligence.Contact.email.exact("sarah.chen@acme.com"),
            SalesIntelligence.Contact.email.exact("james.liu@acme.com"),
        ),
        **base_kwargs,
    )
    print("  Updated Acme Corp deal via link_to")

    # Update contact role — pin to exact email
    client.memory.add(
        content=(
            "Sarah Chen has been promoted to SVP Engineering at Acme Corp. "
            "She's now the decision maker for our deal, not just the champion. "
            "LinkedIn: linkedin.com/in/sarahchen"
        ),
        link_to=build_link_to(
            SalesIntelligence.Contact.email.exact("sarah.chen@acme.com"),
        ),
        **base_kwargs,
    )
    print("  Updated Sarah Chen's role via link_to")


# ---------------------------------------------------------------------------
# 6. EXAMPLE: MEMORY-LEVEL POLICY OVERRIDE
# ---------------------------------------------------------------------------

def policy_override_example(client: Papr, namespace_id: Optional[str] = None):
    """Override schema-level policy for a specific memory."""
    print("\nMemory-level policy override...")

    base_kwargs = {}
    if namespace_id:
        base_kwargs["namespace_id"] = namespace_id

    # Force exact match on deal name (override schema's semantic match)
    # and set a specific loss reason
    client.memory.add(
        content="Sondera.ai deal is lost — they went with a competitor solution.",
        memory_policy=build_memory_policy(
            schema_id="ai_sales_platform",
            node_constraints=[{
                "node_type": "Deal",
                "create": "upsert",
                "search": {"properties": [
                    {"name": "name", "mode": "semantic", "threshold": 0.85},
                ]},
                "set": serialize_set_values({
                    "stage": "lost",
                    "loss_reason": "competitor",
                    "deal_risk": "critical",
                }),
            }],
        ),
        **base_kwargs,
    )
    print("  Marked Sondera.ai deal as lost with policy override")


# ---------------------------------------------------------------------------
# 7. PRINT SCHEMA FOR INSPECTION
# ---------------------------------------------------------------------------

def print_schema():
    """Print the generated schema params for inspection."""
    params = build_schema_params(SalesIntelligence)
    print("\n" + "=" * 60)
    print("GENERATED SCHEMA (what gets sent to the API)")
    print("=" * 60)
    print(json.dumps(params, indent=2, default=str))


# ---------------------------------------------------------------------------
# 8. ATTIO FIELD MAPPING REFERENCE
# ---------------------------------------------------------------------------

def print_attio_mapping():
    """Print the complete Attio → Papr field mapping."""
    print("\n" + "=" * 60)
    print("ATTIO → PAPR FIELD MAPPING")
    print("=" * 60)

    print("""
COMPANY (Attio: 34 attributes → Papr: 10 props + edges + computed)
──────────────────────────────────────────────────────────────────
  Attio Field              → Papr                    Type
  ─────────────            ─────                     ────
  Domains (unique)         → Company.domain           exact() search
  Name                     → Company.name             semantic(0.90)
  Description              → Company.description      string
  Categories (multi-select)→ Company.categories        array
  Primary location         → Company.location         string
  LinkedIn                 → Company.linkedin          string
  Estimated ARR (select)   → Company.estimated_arr     enum
  Employee range (select)  → Company.employee_range    enum
  Funding raised (currency)→ Company.funding_raised    string
  NEW: Deal risk           → Company.deal_risk         enum (AI-assessed)
  ─────────────────────────────────────────────────────────────
  Team (relationship)      → works_at edge (reverse)
  Associated deals (rel)   → deal_with edge (reverse)
  ─────────────────────────────────────────────────────────────
  First/Last/Next interactions → computed from Interaction edges
  Connection strength      → computed from Contact edges
  Strongest connection     → computed from Contact edges
  Twitter follower count   → enrichment (future)
  Logo URL                 → enrichment (future)
  AngelList, Facebook,     → enrichment (future)
    Instagram, Twitter
  Foundation date          → enrichment (future)
  ─────────────────────────────────────────────────────────────
  Record ID, Created at,   → auto-handled by Papr
  Created by, List entries

CONTACT (Attio: 32 attributes → Papr: 10 props + edges + computed)
──────────────────────────────────────────────────────────────────
  Attio Field              → Papr                    Type
  ─────────────            ─────                     ────
  Email addresses (unique) → Contact.email            exact() search
  Name (personal name)     → Contact.name             semantic(0.90)
  Description              → Contact.description      string
  Job title                → Contact.title            string
  Phone numbers            → Contact.phone            string
  Primary location         → Contact.location         string
  LinkedIn                 → Contact.linkedin          string
  Twitter                  → Contact.twitter           string
  Connection strength (sel)→ Contact.connection_strength enum (AI-enhanced)
  NEW: Buying role         → Contact.role              enum (AI-assessed)
  ─────────────────────────────────────────────────────────────
  Company (relationship)   → works_at edge
  Associated deals (rel)   → involves edge (reverse)
  Associated users (rel)   → (internal, not modeled)
  ─────────────────────────────────────────────────────────────
  First/Last/Next interactions → computed from Interaction edges
  Strongest connection     → computed from interaction frequency
  Twitter follower count   → enrichment (future)
  Avatar URL               → enrichment (future)
  AngelList, Facebook,     → enrichment (future)
    Instagram
  ─────────────────────────────────────────────────────────────
  Record ID, Created at,   → auto-handled by Papr
  Created by, List entries

DEAL (Attio: 14 attributes → Papr: 10 props + edges)
──────────────────────────────────────────────────────────────────
  Attio Field              → Papr                    Type
  ─────────────            ─────                     ────
  Deal name (required)     → Deal.name                semantic(0.85)
  Deal stage (required)    → Deal.stage               enum (7 values)
  Deal owner (required)    → Deal.owner               string
  Deal value (currency)    → Deal.value               string
  Source (select)          → Deal.source              enum
  Loss reason (select)     → Deal.loss_reason          enum
  Win reason (select)      → Deal.win_reason           enum
  Next due task            → Deal.next_task            string
  NEW: Deal risk           → Deal.deal_risk            enum (AI-assessed)
  NEW: Win probability     → Deal.win_probability      string (AI-assessed)
  ─────────────────────────────────────────────────────────────
  Associated people (rel)  → involves edge
  Associated company (rel) → deal_with edge
  ─────────────────────────────────────────────────────────────
  Record ID, Created at,   → auto-handled by Papr
  Created by, List entries
""")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="AI Sales Intelligence — Papr Memory Cookbook")
    parser.add_argument(
        "--skip-schema",
        action="store_true",
        default=False,
        help=(
            "Skip schema registration (use when schema already exists). "
            "Set PAPR_SCHEMA_ID in .env to the existing schema ID."
        ),
    )
    parser.add_argument(
        "--skip-seed",
        action="store_true",
        default=False,
        help="Skip seeding controlled vocabulary (Intents + Stages).",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        default=False,
        help=(
            "Start fresh: delete all existing memories for external_user_id "
            "'test@papr.ai', then re-register schema and re-seed vocabulary. "
            "Use this to reset the graph and start over cleanly."
        ),
    )
    args = parser.parse_args()

    print("=" * 60)
    print("AI Sales Intelligence — Papr Memory Cookbook")
    print("=" * 60)

    # Check for API key
    api_key = os.environ.get("PAPR_MEMORY_API_KEY")
    if not api_key:
        print("\nNo PAPR_MEMORY_API_KEY found. Printing schema + mapping only.\n")
        print_schema()
        print_attio_mapping()
        return

    client = Papr(timeout=120.0)

    namespace_id = os.environ.get("PAPR_NAMESPACE_ID")
    schema_id = os.environ.get("PAPR_SCHEMA_ID")
    print(f"Namespace ID : {namespace_id}")
    print(f"Schema ID    : {schema_id or '(will be created)'}")

    # Step 0: Fresh start — delete all existing memories + schema, then re-create
    if args.fresh:
        print("\n--- FRESH START ---")
        print("Deleting all memories for external_user_id='test@papr.ai' "
              f"in namespace '{namespace_id}'...")
        try:
            del_response = client.memory.delete_all(
                external_user_id="test@papr.ai",
                # Pass namespace_id so deletion is scoped to this namespace.
                # NOTE: server-side namespace filtering requires server support;
                # currently deletes all memories for the resolved external user.
                extra_query={"namespace_id": namespace_id} if namespace_id else {},
            )
            print(f"  Status : {del_response.status}")
            print(f"  Deleted: {del_response.total_successful}")
            if del_response.total_failed:
                print(f"  Failed : {del_response.total_failed}")
        except Exception as e:
            print(f"  Delete returned: {e}  (may be first run with no memories)")

        # Delete existing schema so we can re-create with updated definitions
        if schema_id:
            print(f"Deleting existing schema {schema_id}...")
            try:
                client.schemas.delete(schema_id)
                print("  Schema deleted.")
            except Exception as e:
                print(f"  Schema delete failed: {e}")

        # Force schema + seed re-creation on fresh start
        args.skip_schema = False
        args.skip_seed = False
        print("--- Will re-create schema + seed vocabulary ---\n")

    # Step 1: Register schema (skippable)
    if args.skip_schema:
        if not schema_id:
            print("\nWARNING: --skip-schema used but PAPR_SCHEMA_ID is not set in .env.")
            print("         Schema-linked memory_policy calls may not resolve correctly.")
        else:
            print(f"  Skipping schema registration — using existing schema {schema_id}")
    else:
        register_schema(client, namespace_id)

    # Step 2: Seed controlled vocabulary (skippable)
    if args.skip_seed:
        print("  Skipping vocabulary seed.")
    else:
        seed_intents_and_stages(client, namespace_id)

    # Step 3: Feed sample conversations
    feed_conversations(client, namespace_id)

    # Step 4: Targeted updates with link_to
    targeted_updates(client, namespace_id)

    # Step 5: Policy override example
    policy_override_example(client, namespace_id)

    # Print schema + mapping
    print_schema()
    print_attio_mapping()

    print("\n" + "=" * 60)
    print("Done! Your AI Sales Intelligence graph is populated.")
    print("")
    print("What happened automatically:")
    print("  Companies: Acme Corp, Luminary AI")
    print("  Contacts: Sarah Chen, James Liu, Priya Patel, Maya Goldberg")
    print("  Deals: Acme Corp ~$100K, Luminary AI ~$48K/yr")
    print("  Intents: pricing_inquiry, technical_evaluation,")
    print("    competitor_comparison, stakeholder_alignment, champion_identified")
    print("  Competitors: Datadog, MongoDB Atlas")
    print("  Stages: discovery → testing → proposal_contract")
    print("  Deal risk: auto-assessed from conversation signals")
    print("  Connection strength: auto-assessed per contact")
    print("  Buying roles: auto-detected per contact")
    print("  Action items: extracted from every interaction")
    print("")
    print("Query your graph via GraphQL at dashboard.papr.ai")
    print("=" * 60)


if __name__ == "__main__":
    main()
