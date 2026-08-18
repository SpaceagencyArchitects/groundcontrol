# /mobility-analysis

Transit and mobility site analysis for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Provide a Western Australian address and get train and bus access, walk/transit/bike scores, road hierarchy, airport distances, and pedestrian and cycling infrastructure — sourced from Transperth, the PTA, Main Roads WA, and other government data.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

## Install

```bash
# Via plugin system
claude plugin marketplace add SpaceagencyArchitects/groundcontrol
claude plugin install groundcontrol@groundcontrol

# Or symlink just this skill
git clone https://github.com/SpaceagencyArchitects/groundcontrol.git
ln -s $(pwd)/groundcontrol/plugins/groundcontrol/skills/mobility-analysis ~/.claude/skills/mobility-analysis
```

## Usage

```
/mobility-analysis 48 Swanbourne St, Fremantle WA 6160
```

Or start with no context:

```
/mobility-analysis
```

The skill researches:

- **Public transit (Transperth)** — nearest train stations and bus stops, line, walking distance in metres and walk time; SmartRider fare zone for metro sites
- **Walk / Transit / Bike scores** — from walkscore.com (note: sparser data for Australian addresses)
- **Roads & driving** — Main Roads WA road hierarchy, freeways, key intersections, Perth Airport (or nearest regional airport) access
- **Pedestrian & cycling** — footpaths, Principal Shared Paths, the Principal Bike Network, end-of-trip facilities, and current e-scooter / bike-share operators

Output is saved as a markdown file in the working directory (`./mobility-analysis-[location-slug].md`).

## Data Sources

Only governmental, transit authority, and non-profit sources are used. Commercial mapping and real estate platforms are never used.

| Source | Data |
|--------|------|
| Transperth | Train and bus routes, stations, timetables, journey planner |
| PTA WA | Public Transport Authority — service planning, network |
| Main Roads WA | State road network, road hierarchy, traffic volumes |
| Department of Transport WA | Bike network, PSP, active transport |
| Walk Score | Walk / Transit / Bike scores |
| Perth Airport | Airport facilities, terminals |
| LGA online maps | Local bike paths, footpaths, parking restrictions |
| BITRE | National transport statistics |

For overseas projects the skill falls back to the relevant local transit authority.

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Research workflow, output template, preferred sources, guidelines |

## License

MIT
