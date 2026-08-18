# /environmental-analysis

Climate and environmental site analysis for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Provide a Western Australian address and get temperature, precipitation, wind, sun angles, flood, bushfire, seismic risk, soil, and topography — sourced from BoM, Geoscience Australia, DFES, DWER, DBCA, and other governmental and scientific databases.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

## Install

```bash
# Via plugin system
claude plugin marketplace add SpaceagencyArchitects/groundcontrol
claude plugin install groundcontrol@groundcontrol

# Or symlink just this skill
git clone https://github.com/SpaceagencyArchitects/groundcontrol.git
ln -s $(pwd)/groundcontrol/plugins/groundcontrol/skills/environmental-analysis ~/.claude/skills/environmental-analysis
```

## Usage

```
/environmental-analysis 48 Swanbourne St, Fremantle WA 6160
```

Or start with no context:

```
/environmental-analysis
```

The skill researches two sections:

1. **Climate** — monthly temperature normals, precipitation, prevailing winds (incl. diurnal cycles like the Fremantle Doctor), sun angles, NCC climate zone, Köppen classification, humidity, design temperatures, reference evapotranspiration
2. **Natural Features & Hazards** — topography (m AHD), LGA flood mapping, DFES bushfire-prone area status, coastal setbacks (SPP 2.6), seismic risk, soil landscape and engineering classification, acid sulfate soils, vegetation and TECs, water bodies, DWER contamination status

Output is saved as a markdown file in the working directory (`./environmental-analysis-[location-slug].md`).

## Data Sources

Only governmental, university, and non-profit sources are used. Commercial weather aggregators (Weather Spark, Weatherzone consumer pages, climate-data.org) are never used.

| Source | Data |
|--------|------|
| BoM Climate Data Online | Station data — daily / monthly normals, extremes, wind roses |
| BoM Climate Statistics | 1991–2020 normals tables for WA stations |
| BoM Solar Radiation | Daily and monthly solar exposure |
| NCC Climate Zone Map | Climate zone per NCC 2022 |
| Geoscience Australia (ELVIS) | Elevation, topography, contour data |
| Geoscience Australia — Earthquake Hazard | Seismic hazard maps, historical events |
| DFES Bush Fire Prone Areas Map | BPA designation per OBRM |
| WAPC MyPlan | State overlays — BPA, coastal, MRS reservations |
| DWER Contaminated Sites Database | Site contamination classifications |
| DWER Acid Sulfate Soils Mapping | ASS risk mapping |
| NatureMap (DBCA) | Threatened species, TECs, vegetation |
| DPIRD Soil Landscape Mapping | Soil landscape units, engineering classifications |
| Department of Water — Bore Data | Groundwater levels |
| LGA floodplain and coastal hazard (CHRMAP) mapping | Flood SCAs, coastal setbacks |

For overseas projects the skill falls back to international sources (WMO World Weather, USGS Global Seismic Hazard, local flood mapping).

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Research workflow, output template, preferred sources, guidelines |

## License

MIT
