# Papr Python API library

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/papr_memory.svg?label=pypi%20(stable))](https://pypi.org/project/papr_memory/)

The Papr Python library provides convenient access to the Papr REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated with [Stainless](https://www.stainless.com/).

## MCP Server

Use the Papr MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=%40papr%2Fmemory-mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBwYXByL21lbW9yeS1tY3AiXSwiZW52Ijp7IlBBUFJfTUVNT1JZX0FQSV9LRVkiOiJNeSBYIEFQSSBLZXkiLCJQQVBSX01FTU9SWV9TZXNzaW9uX1Rva2VuIjoiTXkgWCBTZXNzaW9uIFRva2VuIiwiUEFQUl9NRU1PUllfQkVBUkVSX1RPS0VOIjoiTXkgQmVhcmVyIFRva2VuIn19)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22%40papr%2Fmemory-mcp%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40papr%2Fmemory-mcp%22%5D%2C%22env%22%3A%7B%22PAPR_MEMORY_API_KEY%22%3A%22My%20X%20API%20Key%22%2C%22PAPR_MEMORY_Session_Token%22%3A%22My%20X%20Session%20Token%22%2C%22PAPR_MEMORY_BEARER_TOKEN%22%3A%22My%20Bearer%20Token%22%7D%7D)

> Note: You may need to set environment variables in your MCP client.

## Documentation

The REST API documentation can be found on [platform.papr.ai](https://platform.papr.ai). The full API of this library can be found in [api.md](api.md).

### Additional Documentation

- **[On-Device Processing](docs/ONDEVICE_PROCESSING.md)** - Guide to enabling local processing with ChromaDB and embedding models
- **[Logging](docs/LOGGING.md)** - Configuration and usage of the logging system
- **[Cleanup](docs/CLEANUP.md)** - Information about data cleanup and uninstall procedures
- **[Tier0 Comparison](docs/TIER0_COMPARISON.md)** - Performance comparison between server-side and local tier0 search

## Installation

```sh
# install from PyPI
pip install papr_memory
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from papr_memory import Papr

client = Papr(
    x_api_key=os.environ.get("PAPR_MEMORY_API_KEY"),  # This is the default and can be omitted
)

# Add a memory
response = client.memory.add(
    content="The project deadline was moved to March 15th. Team agreed to prioritize the auth module first.",
)
print(response.status)  # "success"

# Search memories
results = client.memory.search(
    query="What is the project deadline?",
    max_memories=10,
    rank_results=True,
)
for memory in results.data.memories:
    print(memory.content)
```

While you can provide a `bearer_token` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `PAPR_MEMORY_BEARER_TOKEN="My Bearer Token"` to your `.env` file
so that your Bearer Token is not stored in source control.

## Graph Schemas & Memory Policies

Schemas define the structure of your knowledge graph. When you add memories, the engine uses the schema to extract entities from the content, match them to existing nodes, and build relationships automatically.

### 1. Define a Schema

```python
from papr_memory.lib import (
    schema, node, lookup, upsert, constraint,
    prop, edge, exact, semantic, Auto,
    build_schema_params,
)

@schema("project_tracker")
class ProjectSchema:

    @node
    @lookup  # Only match existing people, never create new ones
    class Person:
        name: str = prop(required=True, search=semantic(0.90))
        email: str = prop(search=exact())

    @node
    @upsert  # Create or update tasks as they're mentioned
    @constraint(
        set={"status": Auto()},  # LLM infers status from memory content
    )
    class Task:
        title: str = prop(required=True, search=semantic(0.85))
        status: str = prop(enum_values=["open", "in_progress", "done"])

    works_on = edge(Person, Task, create="upsert")

# Register the schema once
params = build_schema_params(ProjectSchema)
client.schemas.create(**params)
```

### 2. Just Add Memories

Once the schema is registered, just pass your content. The engine auto-detects the matching schema and applies the policies you defined:

```python
# Meeting transcript - just pass the content
client.memory.add(
    content="John (john@papr.ai) mentioned he fixed the authentication bug. It's now resolved.",
)
```

That's it. Here's what happens automatically:

1. **Schema matching** - The engine detects that this content matches the `project_tracker` schema (it contains a person and a task)
2. **Entity extraction** - Identifies "John" / "john@papr.ai" as a Person and "authentication bug" as a Task
3. **Node matching** - Finds the existing Task whose `title` semantically matches "authentication bug" (0.85 threshold) and the Person whose `email` exactly matches "john@papr.ai"
4. **Resolution policies** - Task is `@upsert` so it gets updated. Person is `@lookup` so it only matches existing people, never creates new ones
5. **Constraints** - `@constraint(set={"status": Auto()})` tells the LLM to infer status from context. Since the content says "fixed" and "resolved", it sets `status: "done"`. Use `Auto("prompt")` to provide per-field extraction guidance (e.g. `Auto("Summarize in 1-2 sentences")`)
6. **Edge creation** - A `WORKS_ON` edge is created between John and the task

> **Tip:** Include identifiers like emails or IDs in your content (e.g. `"John (john@papr.ai)"`) to help the engine match the right nodes via `exact()` search properties.

### 3. More Control with `link_to`

For cases where you want to explicitly direct which nodes to match, use `link_to`:

```python
from papr_memory.lib import build_link_to

# Tell the engine exactly which properties to search
client.memory.add(
    content="The authentication bug is now resolved.",
    link_to=build_link_to(
        ProjectSchema.Task.title,  # -> "Task:title" (semantic match from schema)
    ),
)

# Pin to a specific value when you know it
client.memory.add(
    content="Sprint update: auth module is done.",
    link_to=build_link_to(
        ProjectSchema.Task.title.exact("Fix authentication bug"),
        ProjectSchema.Person.email.exact("john@papr.ai"),
    ),
)
# -> link_to=["Task:title=Fix authentication bug", "Person:email=john@papr.ai"]
```

### 4. Memory-Level Policy Overrides

Schema defines the default behavior. For specific memories that need different handling, override per-memory with `memory_policy`:

```python
from papr_memory.lib import build_memory_policy, serialize_set_values, Auto

# Override: force exact match and set priority for this specific memory
client.memory.add(
    content="TASK-456 is now critical priority",
    memory_policy=build_memory_policy(
        schema_id="project_tracker",
        node_constraints=[{
            "node_type": "Task",
            "create": "upsert",
            "search": {"properties": [{"name": "title", "mode": "exact"}]},
            "set": serialize_set_values({"priority": Auto()}),
        }],
    ),
)
```

### Resolution Policies

| Decorator | Policy | Use Case |
|-----------|--------|----------|
| `@upsert` | Create if not found, update if exists | Dynamic entities (tasks, conversations, events) |
| `@lookup` | Only match existing nodes, never create | Controlled data (people from directory, product catalog) |
| `@resolve(on_miss="error")` | Fail if not found | Strict validation (required references) |

### Search Modes

```python
id: str = prop(search=exact())            # Exact string match
title: str = prop(search=semantic(0.85))   # Embedding similarity (threshold 0.85)
name: str = prop(search=fuzzy(0.80))       # Levenshtein distance (threshold 0.80)
```

### Conditional Constraints

```python
from papr_memory.lib import And, Or, Not, Auto

@node
@upsert
@constraint(
    when=And(
        Or({"severity": "high"}, {"severity": "critical"}),
        Not({"status": "resolved"}),
    ),
    set={
        "flagged": True,
        "summary": Auto("Summarize the security incident in 1-2 sentences"),
    },  # Auto("prompt") guides LLM extraction; Auto() with no args also works
)
class Alert:
    alert_id: str = prop(search=exact())
    title: str = prop(required=True, search=semantic(0.85))
    severity: str = prop()
    status: str = prop()
    flagged: bool = prop()
    summary: str = prop()
```

### Complete Example: Security Monitoring

```python
from papr_memory.lib import (
    schema, node, lookup, upsert, resolve, constraint,
    prop, edge, exact, semantic, Auto,
    build_schema_params, build_link_to,
)

@schema("security_monitoring")
class SecuritySchema:

    @node
    @lookup
    class TacticDef:
        """MITRE ATT&CK tactic (pre-loaded reference data)."""
        id: str = prop(search=exact())
        name: str = prop(required=True, search=semantic(0.90))

    @node
    @upsert
    class SecurityBehavior:
        description: str = prop(required=True, search=semantic(0.85))
        severity: str = prop(enum_values=["low", "medium", "high", "critical"])

    @node
    @upsert
    @constraint(
        when={"severity": "critical"},
        set={"flagged": True, "reviewed_by": Auto()},
    )
    class Alert:
        alert_id: str = prop(search=exact())
        title: str = prop(required=True, search=semantic(0.85))
        severity: str = prop()
        flagged: bool = prop()
        reviewed_by: str = prop()

    mitigates = edge(
        SecurityBehavior, TacticDef,
        search=(TacticDef.id.exact(), TacticDef.name.semantic(0.90)),
        create="lookup",
    )

    triggers = edge(SecurityBehavior, Alert, create="upsert")

# Register schema
params = build_schema_params(SecuritySchema)
client.schemas.create(**params)

# Add memory - graph is built automatically
client.memory.add(
    content="Detected credential stuffing attack targeting admin accounts",
    link_to=build_link_to(
        SecuritySchema.TacticDef.name.semantic(0.90, "credential access"),
        SecuritySchema.Alert.title,
    ),
)
```

## Async usage

Simply import `AsyncPapr` instead of `Papr` and use `await` with each API call:

```python
import os
import asyncio
from papr_memory import AsyncPapr

client = AsyncPapr(
    x_api_key=os.environ.get("PAPR_MEMORY_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    user_response = await client.user.create(
        external_id="demo_user_123",
        email="user@example.com",
    )
    print(user_response.external_id)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install papr_memory[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from papr_memory import DefaultAioHttpClient
from papr_memory import AsyncPapr


async def main() -> None:
    async with AsyncPapr(
        x_api_key=os.environ.get("PAPR_MEMORY_API_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        user_response = await client.user.create(
            external_id="demo_user_123",
            email="user@example.com",
        )
        print(user_response.external_id)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from papr_memory import Papr

client = Papr()

memory = client.memory.update(
    memory_id="memory_id",
    graph_generation={},
)
print(memory.graph_generation)
```

## File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, or a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from papr_memory import Papr

client = Papr()

client.document.upload(
    file=Path("/path/to/file"),
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `papr_memory.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `papr_memory.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `papr_memory.APIError`.

```python
import papr_memory
from papr_memory import Papr

client = Papr()

try:
    client.user.create(
        external_id="demo_user_123",
        email="user@example.com",
    )
except papr_memory.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except papr_memory.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except papr_memory.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from papr_memory import Papr

# Configure the default for all requests:
client = Papr(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).user.create(
    external_id="demo_user_123",
    email="user@example.com",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from papr_memory import Papr

# Configure the default for all requests:
client = Papr(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Papr(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).user.create(
    external_id="demo_user_123",
    email="user@example.com",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `PAPR_LOG` to `info`.

```shell
$ export PAPR_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from papr_memory import Papr

client = Papr()
response = client.user.with_raw_response.create(
    external_id="demo_user_123",
    email="user@example.com",
)
print(response.headers.get('X-My-Header'))

user = response.parse()  # get the object that `user.create()` would have returned
print(user.external_id)
```

These methods return an [`APIResponse`](https://github.com/Papr-ai/papr-pythonSDK/tree/main/src/papr_memory/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/Papr-ai/papr-pythonSDK/tree/main/src/papr_memory/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.user.with_streaming_response.create(
    external_id="demo_user_123",
    email="user@example.com",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from papr_memory import Papr, DefaultHttpxClient

client = Papr(
    # Or use the `PAPR_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from papr_memory import Papr

with Papr() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Papr-ai/papr-pythonSDK/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import papr_memory
print(papr_memory.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
