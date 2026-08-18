# /studio — Studio Router

Describe your task and get routed to the right agent or skill. Start here if you don't know which of 19 skills to call.

## Usage

```
/studio [describe what you need]
```

## Examples

| Input | Routes to |
|-------|-----------|
| `/studio task chair, mesh back, under $800` | Product & Materials Researcher agent |
| `/studio 48 Swanbourne St, Fremantle WA` | Asks: site context or zoning? |
| `/studio where do the wall finishes go?` | GROUNDCONTROL codex |
| `/studio make a deck from this report` | `/slide-deck-generator` |

## How It Works

1. Reads your input and classifies intent
2. Routes to the right agent or skill — no keyword matching, just natural language understanding
3. If ambiguous, asks one clarifying question
4. Loads the agent file at runtime and follows its workflow

The router contains no orchestration logic. Agent files are the single source of truth.

## License

MIT
