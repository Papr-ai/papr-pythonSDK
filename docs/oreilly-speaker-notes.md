# O'Reilly AI Superstream: Context Engineering — Speaker Notes
## "Building the Brain: How Predictive Memory Transforms AI Agents"
### Shawkat Kabbara | Feb 26, 2026

**Total runtime:** 25 minutes (15 min slides + 10 min demo)

---

## Slide 1: Title (30 sec)

**On screen:** "Building the Brain: How Predictive Memory Transforms AI Agents" — Shawkat Kabbara, Founder & CEO, Papr

**Say:**

> Thanks for joining. I'm Shawkat, founder of Papr. Over the next 25 minutes, I'm going to show you how we built a memory system for AI agents inspired by how the human brain actually works — and why memory is prediction, not search.
>
> We'll look at real production data, and I'll do a live demo where we go from schema definition to an intelligent application. No ML team required.

**Timing note:** Keep it tight — 30 seconds max. Don't over-introduce yourself. This is Zoom — no audience visible, they can chat or ask questions live.

---

## Slide 2: "Memory Supercharges Agents — Then KILLS Them at Scale" (2 min)

**On screen:** 2x2 grid — Latency Explodes (200ms to 3s), Accuracy Plummets (vector search returns noise), Engineering Burns (teams maintain pipelines), Time Wasted (constant retuning)

**Say:**

> Let me tell you how we got here. When ChatGPT 3.5 launched, I tried to build what I thought was a straightforward product — a project manager agent. Something that could actually manage projects, not just answer questions about them.
>
> I realized pretty quickly: to be useful, this agent needed context. It needed conversations, documents, meeting notes, emails — structured and unstructured data. It needed to remember what happened last week in the standup, who owns which task, what the client said in that email three days ago.
>
> So we built memory. And at first it was magic — the PM agent went from useless to genuinely helpful. But then something happened.
>
> The more memory we added, the WORSE the agent got. Not better — worse. Latency exploded — what was 200ms became 3 seconds. The vector search started returning noise instead of the relevant meeting note from Tuesday. We were spending all our time tuning the retrieval pipeline instead of building features.
>
> So we tried to measure it. And that's when we saw this pattern clearly.
>
> [gesture to slide]
>
> These four problems hit every team building agents with memory. Latency explodes. Accuracy plummets. Engineering burns out maintaining pipelines. Months wasted retuning, never shipping.
>
> If any of you have hit this wall — and I'd bet most of you have — drop it in the chat. This is the fundamental tension: memory is what makes agents useful, but memory at scale is what kills them. Our answer to this started with a question from neuroscience.

**Key beats:**
- This is YOUR origin story — be conversational, not scripted. Let it feel like you're telling a friend
- "ChatGPT 3.5 launched" grounds the timeline — everyone remembers that moment
- The twist ("the more memory, the WORSE it got") is the hook — pause slightly before "worse"
- "So we tried to measure it" — sets up the rest of the talk as the solution to a real problem you lived
- "Drop it in the chat" replaces show-of-hands for Zoom format
- End with the neuroscience hook to transition to Slide 3

---

## Slide 3: "Your Brain Doesn't Search. It Predicts." (1 min 30 sec)

**On screen:** Left: "THE OLD WAY (Reactive)" — Query > Index > Search > Rerank > Result = High Latency. Right: "THE PAPR WAY (Proactive)" — Context Cues > Prediction > Pre-staged Memory > Instant Availability = Zero Latency. Quote at bottom: "The hippocampus pre-stages memories based on context before you consciously recall them. We built an architecture that does the same."

**Say:**

> When you walk into a kitchen, your brain doesn't Google for "cooking-related memories." Before you even decide to cook, your hippocampus has already activated cooking memories, recipe patterns, spatial layouts — all based on context cues. The brain PREDICTS what memories you'll need and pre-stages them.
>
> Every agent memory system today works the other way. Look at the left side — an agent asks a question, a retrieval call fires, it indexes, searches, reranks, results come back. That's search, not memory. It's fine for simple Q&A, but it breaks when agents need to reason across long histories, multiple tools, or real-time context.
>
> Papr flips the model. Instead of retrieve-then-reason, it's anticipate-then-retrieve. If we know you're working on a deal with Acme Corp, your contact history, pricing precedents, and relevant Slack threads are already cached before you ask.

**Key beats:**
- The kitchen analogy is memorable — use it to anchor the concept
- Point to left/right sides of the slide as you compare
- "Anticipate-then-retrieve" is the phrase that should stick

---

## Slide 4: "4-Tier Memory Architecture: Edge to Cloud" (1 min)

**On screen:** Inverted pyramid — Tier 0: Working, Tier 1: Episodic, Tier 2: Vector, Tier 3: Graph. Callout: "91% of queries are served by predicted groupings at Tier-2."

**Say:**

> Here's the architecture. Four tiers from edge to cloud.
>
> Tier-0 is your working set — the 500 memories most likely needed right now, predicted from your goals and recent activity. Under 10 milliseconds.
>
> Tier-1 is on-device episodic memory for slightly broader context. Tier-2 is cloud-based vector search — semantic search via Qdrant. Tier-3 is the full knowledge graph — Neo4j for deep graph traversal when you need maximum accuracy.
>
> The key insight: 91% of production queries are served by predicted groupings at Tier-2. The system gets smarter over time. More data means better predictions, not worse search results. That's the opposite of every retrieval system today.

**Key beats:**
- Walk down the pyramid quickly — don't linger on each tier
- Emphasize the 91% stat — it's the proof the architecture works
- "More data = better predictions, not worse search" — this is counterintuitive and memorable

---

## Slide 5: "The 'Box' Metaphor: Grouped Embeddings" (2 min)

**On screen:** Left: 4 documents (Call, Contract, Pricing, Slack) merging into a "Grouped Embedding" box. Center: "1 Query" arrow hitting the box. Right: Box exploding open, 4 documents fanning out. Bottom stats: 45% Faster, 4x More Context, 72% More Relevant.

**Say:**

> This is the core innovation — let me walk you through it.
>
> When a new memory is indexed — say a sales call transcript — the system finds the top 3 semantically related memories. Maybe it's the customer's contract history, a pricing discussion, and a relevant Slack thread. It takes all 4 memories, creates a grouped embedding that captures the aggregate semantic space, and indexes that alongside the individual embeddings.
>
> At search time, when a query hits this grouped embedding, it's like opening a box — one ANN hit returns all 4 related memories together. Instead of needing 4 separate search hits to find contextually related information, you get it all in one.
>
> This is how the brain works. You don't recall "Acme Corp" and then separately recall "their Q3 pricing discussion" — they fire together because they're stored in the same neural cluster.
>
> And the results speak for themselves: 45% faster because fewer round-trips, 4x more context per query, and 72% more relevant based on semantic similarity scores.

**Key beats:**
- This is your MOST IMPORTANT technical slide — take your time
- Walk through the 3-step flow (index > search > result) visually
- The brain analogy ("fire together") reinforces the neuroscience framing
- End on the three stats — let them land

---

## Slide 6: "Stanford STARK Benchmark: Latest Evaluation" (1 min)

**On screen:** Horizontal bar chart — Papr: 92%, 2nd Best: 58%, 3rd Best: 53%, 4th Best: 47%.

**Say:**

> Does this actually work at benchmark scale? Yes.
>
> Stanford STARK is the standard benchmark for semi-structured retrieval. It tests whether a system can accurately find information across documents with complex relationships — exactly what agents need.
>
> Papr: 92% Hit@5. Second best in the field: 58%. That's not an incremental improvement — it's a different class of performance. And this is up from 86% six months ago, because the predictive grouping system improves with more data.
>
> The formula we use captures both accuracy AND latency in one metric, so you can't game it by being fast but wrong, or accurate but slow.

**Key beats:**
- Let the chart speak — the visual gap between 92% and 58% is dramatic
- "Different class of performance" — confident but not arrogant
- Mention it improved from 86% to 92% — shows trajectory

---

## Slide 7: "Live Demo: Fast & Relevant Search with Voice Input" (30 sec)

**On screen:** Video player mockup — "Fast Search" with voice input. "Showcasing the speed and relevance of the results."

**Say:**

> Before we go into schemas and how you actually build with this, let me quickly show you what the end-user experience looks like. This is real-time search with voice input — notice the speed and relevance of the results.
>
> [Play brief clip or describe: sub-second retrieval, relevant results from natural language query]
>
> That's the experience predictive memory enables. Now let me show you how to build systems that deliver this.

**Key beats:**
- This is a quick taste of the demo to build excitement
- If playing a video clip, keep it under 20 seconds
- Transition quickly to the schema slides

---

## Slide 8: "Define a Schema. Get a Knowledge Graph." (1 min 30 sec)

**On screen:** Python-like schema code — `@schema("ai_sales_platform")` with `@node` Company, `@node @controlled_vocabulary` Intent and Stage classes. Annotations: "Forces LLM to link to existing business concepts" and "Policy that prevents graph pollution."

**Say:**

> This is how you use Papr. You define a schema — what entities matter in your domain, their properties, and how they relate.
>
> Two key concepts. `@node` means this is an entity type — Company, Contact, Interaction. `@controlled_vocabulary` means "this is a pre-defined list — never create new ones, only link to existing." Intent and Stage are controlled vocabularies — you pre-define your sales intents and pipeline stages, and the system only links to them.
>
> This is critical for accuracy. Without controlled vocabularies, your LLM will hallucinate intent categories — "pricing discussion" vs "price inquiry" vs "cost question" — all slightly different, polluting your graph. With controlled vocabulary, it MUST match to your pre-defined list. `create="never"` is the policy that enforces this.
>
> These 30 lines of schema define your entire sales intelligence ontology.

**Key beats:**
- Point to the annotations on the slide as you explain them
- The "hallucination prevention" angle resonates — everyone has this problem
- "30 lines" — emphasize simplicity

---

## Slide 9: "Policies in Action: Automatic Graph Extraction" (1 min)

**On screen:** Three-column flow — Input (unstructured call transcript with Sarah Chen) > Extraction & Logic (Sarah Chen > Contact Node; pricing tiers > Intent: pricing_inquiry, Link Only; evaluating > Stage: evaluation, Link Only) > Output (structured graph with Contact, Interaction, Intent, Stage nodes). Bottom: "No regex. No manual pipelines. The Schema *is* the pipeline."

**Say:**

> Here's what happens when you add a sales call transcript. The LLM reads the content and your schema. It extracts entities — Sarah Chen as a Contact, pricing inquiry as an Intent, evaluation as a Stage.
>
> Then the memory policies kick in. Contact is a regular node — if Sarah already exists, merge. If not, create her. Intent is a controlled vocabulary — it searches for "pricing inquiry" against your pre-defined list. Found it? Link. Not found? Skip, don't hallucinate a new one. Same for Stage.
>
> The graph builds itself. No regex. No rules engine. No manual pipelines. The schema IS the pipeline.

**Key beats:**
- Walk left to right through the three columns
- Emphasize "Link Only" — this is what prevents graph pollution
- The bottom tagline ("The Schema IS the pipeline") should land as a mic-drop moment

---

## Slide 10: "Power Intelligent Apps via GraphQL" (1 min)

**On screen:** Left: GraphQL query for DealIntelligence. Right: Sales Intelligence dashboard mockup showing Time to Close (42 Days), Deal Risk (High - Pricing Objection), Win Probability (68%), Intent Signals timeline, and recommendation "Offer Competitor X Comparison Sheet."

**Say:**

> Here's why this matters. Once you have structured graph data, you can power REAL applications — not just chat interfaces.
>
> This is a deal intelligence dashboard. Every card on this screen is powered by a single GraphQL query against the knowledge graph built from your sales calls, emails, and meeting notes.
>
> Time to close, deal risk detected from pricing objections, win probability, intent signals tracked over time — and actionable recommendations. "Offer Competitor X Comparison Sheet" — that's graph traversal finding similar past deals where pricing objections were overcome.
>
> You didn't need a team of data engineers. Schema, memory policies, GraphQL. That's the entire stack.

**Key beats:**
- Point to specific cards as you describe them
- The recommendation card is the "wow" moment — show how graph traversal generates actionable insights
- "Schema, memory policies, GraphQL — entire stack" — drive home simplicity

---

## Slide 11: "Context Intelligence > Context Graphs" (1 min)

**On screen:** Three stacked layers — Bottom: Context Graphs (Decision traces, Temporal context, Relationships). Middle: Predictive Memory (Anticipate needs, Pre-stage context, 4-tier caching). Top: Memory Policies (Schema-controlled extraction, Business rules). Right brace: "CONTEXT INTELLIGENCE"

**Say:**

> There's a lot of buzz right now about "context graphs" — Foundation Capital called it a trillion-dollar opportunity. They're right that capturing the reasoning trace between data and action matters. But a context graph alone is just a better knowledge graph.
>
> Context INTELLIGENCE adds two critical layers. Predictive memory — anticipate what context you need and pre-stage it with our 4-tier architecture. Memory policies — control HOW entities are extracted using your business rules, schemas, and controlled vocabularies.
>
> A context graph stores decision traces. Context intelligence PREDICTS which traces you'll need, extracts them automatically from unstructured data, and serves them at sub-second latency. That's the difference between a database and a brain.

**Key beats:**
- This slide positions Papr in the industry conversation
- "Trillion-dollar opportunity" validates the space
- "Database vs brain" is the closing line — make it land

---

## Slide 12: "The Toolkit: Build It Today" (45 sec)

**On screen:** Three cards — 1. Schema (Define your domain entities and vocabulary), 2. Policies (Control extraction: create='never', upsert), 3. GraphQL (Query the graph for any UI). Bottom left: "What you DON'T need: No vector DB config, No embedding model selection." Bottom right: QR codes for github.com/papr-ai and dashboard.papr.ai.

**Say:**

> Here's the takeaway. To build what I just showed you, you need three things. A schema — define what entities matter. Policies — control how they're extracted and linked. GraphQL — query your graph to power any UI.
>
> What you DON'T need: no vector database configuration, no embedding model selection, no retrieval pipeline engineering. Papr handles all of that.
>
> We're open source — scan the QR code for our GitHub. The dashboard is free to start.
>
> Now let me show you all of this live.

**Key beats:**
- This is the CTA slide before demo — make it actionable
- Point to QR codes
- Transition smoothly into the live demo

---

## LIVE DEMO (10 min)

### Demo Step 1: Show the Schema (2 min)

**What to show:**
- Open Papr dashboard > Schemas view
- Walk through the AI Sales schema: Company, Contact, Intent (controlled vocabulary), Stage (controlled vocabulary), Interaction
- Show edge definitions: `shows_intent`, `at_stage`, `works_at`
- Highlight `@controlled_vocabulary` decorator and `create="never"` policy

**Say:**

> This is our dashboard. I've already set up the AI Sales schema we just talked about. These 30 lines define my entire sales intelligence ontology.
>
> Notice Intent and Stage are marked as controlled vocabularies. I've pre-loaded our sales intents — pricing_inquiry, competitor_mention, budget_discussion, buying_signal — and pipeline stages — discovery, evaluation, negotiation, closed_won, closed_lost.
>
> Let me now feed it some real content.

---

### Demo Step 2: Ingest Content (2 min)

**What to show:**
- Use API call or Playground to `add_memory()` with a sales call transcript
- Show extraction happening in real-time
- Highlight entity extraction and controlled vocabulary matching

**Code to execute:**
```python
await client.add_memory(
    content="""
    Call with Sarah Chen (VP Engineering at Acme Corp):
    - Discussed our pricing tiers in detail
    - Mentioned they're evaluating vs Competitor X
    - Asked about enterprise security features
    - Timeline: Q2 budget approval
    """,
    link={
        Interaction.content.semantic(0.85)
            .shows_intent(Intent.name.semantic(0.95))
            .set({Interaction.channel: "call"}),
        Contact.name.semantic(0.90)
            .works_at(Company.name.semantic(0.90))
    }
)
```

**Say:**

> I'm adding a sales call transcript. Watch what happens.
>
> [wait for extraction]
>
> Notice — Intent matched to "pricing_inquiry" from the controlled vocabulary. It didn't create "price question" or "cost discussion." That's the controlled vocabulary enforcing consistency. Stage matched to "evaluation." Sarah Chen was created as a Contact and linked to Acme Corp.

---

### Demo Step 3: Explore Views (2 min)

**What to show:**
- Dashboard Views: Contact, Intent, Stage, Interaction tables
- Filter contacts by company
- Show how unstructured text became structured, queryable data

**Say:**

> Now let's look at the data. Here are all extracted contacts — filterable by company, title, email. Here are the intent signals detected across all interactions. Here are the pipeline stages.
>
> Every row here was extracted from natural language. No regex. No rules engine. Schema + LLM + memory policies.

---

### Demo Step 4: Explore the Graph (2 min)

**What to show:**
- Graph visualization: nodes and relationships
- Click Contact > see Interactions > see linked Intents
- Show traversal: Contact > works_at > Company; Interaction > shows_intent > Intent

**Say:**

> And here's the knowledge graph. Sarah Chen is connected to Acme Corp via works_at. Her interaction shows_intent links to pricing_inquiry and competitor_mention. The interaction is at_stage evaluation.
>
> This is your sales knowledge graph, built automatically from a call transcript. Click any node to explore relationships, traverse the graph, find patterns.

---

### Demo Step 5: GraphQL Query (2 min)

**What to show:**
- GraphQL Playground or API call
- Query: get all contacts at a company with their intent signals

**Code to execute:**
```graphql
query {
  companies {
    name
    contacts {
      name
      title
      interactions {
        showsIntent {
          name
          strength
        }
      }
    }
  }
}
```

**Say:**

> Finally, GraphQL. One query — get me all companies, their contacts, and what intent signals were detected in their interactions.
>
> [show results]
>
> Typed response, filterable, real-time. This is the same query that powers dashboards like the one I showed you earlier. Build any UI you want on top of this.
>
> That's it — schema, policies, GraphQL. From unstructured call transcript to queryable knowledge graph in under 5 minutes.

---

## Closing (after demo, 30 sec)

**Say:**

> To recap: memory is what makes agents useful, but traditional retrieval breaks at scale. Papr's predictive memory — inspired by how the hippocampus actually works — solves this by anticipating context needs and pre-staging them. Combined with schema-driven extraction and memory policies, you get Context Intelligence, not just context graphs.
>
> We're open source, the dashboard is free. I'd love to see what you build with it. Thank you.

---

## Timing Summary

| Slide | Content | Duration |
|-------|---------|----------|
| 1 | Title | 0:30 |
| 2 | Origin story + pain at scale | 2:00 |
| 3 | Brain predicts, doesn't search | 1:30 |
| 4 | 4-tier architecture | 1:00 |
| 5 | Box metaphor: grouped embeddings | 2:00 |
| 6 | Stanford STARK benchmark (92%) | 1:00 |
| 7 | Quick demo teaser (video/clip) | 0:30 |
| 8 | Schema-driven graph extraction | 1:30 |
| 9 | Policies in action | 1:00 |
| 10 | Power apps via GraphQL | 1:00 |
| 11 | Context Intelligence > Context Graphs | 1:00 |
| 12 | The toolkit: build it today | 0:45 |
| — | **Slides subtotal** | **~13:45** |
| Demo | 5 steps (schema, ingest, views, graph, GraphQL) | **10:00** |
| — | Closing | 0:30 |
| **TOTAL** | | **~24:45** |

*~15 sec buffer. Tight but doable.*

---

## Anticipated Q&A (if time permits)

| Question | Answer |
|----------|--------|
| "How does this compare to Mem0 / Zep?" | "Mem0 is vector-only, no graph, no memory policies. Zep uses Neo4j but no controlled vocabularies, no predictive grouping. We combine vector, graph, predictive memory, and schema-driven policies in one system." |
| "What embedding model do you use?" | "Qwen 4B with 2560-dimensional embeddings for grouped embeddings. The key insight is the grouped embedding captures the aggregate semantic space of related memories." |
| "How does it handle conflicting information?" | "Memory policies with temporal context. Newer memories update existing nodes via upsert. Controlled vocabularies prevent duplication and entity drift." |
| "What's the pricing?" | "Free tier for development. Usage-based in production. Open source on GitHub." |
| "Can I bring my own graph database?" | "Today we use Neo4j and Qdrant. The tight integration between vector and graph is what enables predictive grouping — it's architecturally fundamental, not a plug-in." |
| "How fast is ingestion?" | "Schema extraction typically takes 2-5 seconds depending on content length. The LLM does the heavy lifting, and policies execute in milliseconds." |
| "Does this work for non-sales use cases?" | "Absolutely. The schema system is domain-agnostic. We have users building customer support knowledge bases, research assistants, legal document analysis, developer documentation — any domain with entities and relationships." |

---

## Pre-Demo Checklist

- [ ] Dashboard loaded and logged in
- [ ] AI Sales schema already created
- [ ] Controlled vocabularies pre-loaded (intents, stages)
- [ ] API key ready for live ingestion
- [ ] GraphQL playground open in separate tab
- [ ] Fallback screenshots ready in case of connectivity issues
- [ ] Water bottle nearby
