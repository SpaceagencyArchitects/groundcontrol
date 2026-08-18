# Rules

Rules are always-on conventions that shape every skill output. Unlike skills (invoked with a slash command), rules are loaded automatically and apply across all plugins.

**Default jurisdiction: Western Australia.** All rules below are oriented to Australian and WA practice (NCC, R-Codes, LPS / LPP, NATSPEC, Landgate / SLIP, ABS, BoM, Heritage Council of WA, Architects Board of WA).

| Rule | What it governs |
|------|-----------------|
| [units-and-measurements](./units-and-measurements.md) | Metric (SI) defaults, area types (GFA/NLA/NSA/Plot Ratio), dimension formatting (mm / m), AHD levels |
| [code-citations](./code-citations.md) | NCC, R-Codes, AS/NZS, LPS / LPP, WA legislation — edition years, clause notation, jurisdiction awareness |
| [code-currency](./code-currency.md) | Verify codes / standards / rating-tool versions are the current in-force edition before relying on them; don't assert a fixed edition as current |
| [professional-disclaimer](./professional-disclaimer.md) | Disclaimer language for AI outputs; Architects Act 2004 (WA) framing; what AI outputs can and cannot claim |
| [natspec-formatting](./natspec-formatting.md) | NATSPEC worksection numbers, three-part structure, AS/NZS references, cross-references |
| [terminology](./terminology.md) | Australian AEC terminology, WA planning vocabulary, heritage vocabulary, Australian English spelling |
| [output-formatting](./output-formatting.md) | Tables, headings, source attribution (ABS / Landgate / BoM / inHerit), file naming, list structure |
| [transparency](./transparency.md) | Show your work — link to NCC / R-Codes / LPS / SAT sources, expose inputs, make outputs verifiable |

## How Rules Work

When you install a plugin from this repository, its skills follow these rules automatically. The rules are reference documents — Claude reads them to maintain consistency across all outputs.

Rules are not invoked directly. They inform how skills produce their outputs.
