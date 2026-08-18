# /demographics-analysis

Demographics and market site analysis for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Provide a Western Australian address and get population, income, age distribution, housing market data, and employment statistics — sourced from the ABS Census, .id community profiles, REIWA, and other governmental and industry-body databases.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

## Install

```bash
# Via plugin system
claude plugin marketplace add SpaceagencyArchitects/groundcontrol
claude plugin install groundcontrol@groundcontrol

# Or symlink just this skill
git clone https://github.com/SpaceagencyArchitects/groundcontrol.git
ln -s $(pwd)/groundcontrol/plugins/groundcontrol/skills/demographics-analysis ~/.claude/skills/demographics-analysis
```

## Usage

```
/demographics-analysis 48 Swanbourne St, Fremantle WA 6160
```

Or start with no context:

```
/demographics-analysis
```

The skill researches, reporting at the appropriate ABS geography (SA1 / SA2 / suburb / LGA / Greater Perth):

- **Population** — count, density, 5- and 10-year growth trend, WA Tomorrow / .id projections
- **Income & employment** — median household income, dominant industries and occupations, major nearby employers, LGA / Greater Perth unemployment
- **Age & composition** — median age, cohort breakdown, cultural and linguistic composition, Aboriginal & Torres Strait Islander population
- **Housing market** — REIWA median house and unit prices, rents, dwelling stock, tenure mix

All metrics are benchmarked against Greater Perth and WA figures, with the geographic scale and Census vintage stated. Output is saved as a markdown file in the working directory (`./demographics-analysis-[location-slug].md`).

## Data Sources

Only governmental, university, and industry-association sources are used. Commercial real estate aggregators (realestate.com.au search statistics, Domain, OnTheHouse) are never used — REIWA is the WA industry body and the appropriate suburb data source.

| Source | Data |
|--------|------|
| ABS Census QuickStats | Suburb / SA2 / LGA demographic snapshot |
| ABS DataExplorer | Custom Census tables, time series |
| ABS Community Profiles | Detailed Census profile per geography |
| .id Community (profile.id.com.au) | Community profiles for many WA LGAs |
| .id Forecast (forecast.id.com.au) | LGA population and dwelling forecasts |
| WA Tomorrow | WA Government population projections by LGA |
| REIWA | Suburb median house / unit prices, rents, sales activity |
| ABS Building Approvals | New dwelling approvals by LGA |
| Department of Communities — Housing | Social and affordable housing context |
| RBA Statistical Tables | National economic indicators |
| WA Treasury Economic Data | State-level economic indicators |

For overseas projects the skill falls back to international sources (World Bank Open Data, UN Data, the relevant national statistics agency).

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Research workflow, output template, preferred sources, guidelines |

## License

MIT
