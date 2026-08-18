# Output Formatting

These conventions govern how skill outputs are structured and presented.

## Tables

- Use tables for **all comparative data**: product comparisons, scenario analysis, code requirements, area breakdowns
- Include units in column headers, not in every cell: `Area (SF)` with values `1,250` — not `1,250 SF` in each row
- Right-align numeric columns; left-align text columns
- Always include a totals or summary row where applicable

## Headings

- Structure outputs with clear, hierarchical headings that match professional deliverable conventions
- Use descriptive headings, not generic ones: "Egress Requirements — Level 2" not "Section 3"
- Number headings only when the output is a specification or report with cross-references

## Source Attribution

- Cite the source for every data point that comes from an external database or API:
  - Census / demographics: "Source: Australian Bureau of Statistics (ABS), Census of Population and Housing 2021"
  - Property / cadastral: "Source: Landgate, SLIP (Shared Location Information Platform)"
  - Planning / zoning: "Source: WAPC — Metropolitan Region Scheme" or "Source: City of Fremantle LPS4"
  - Climate / meteorology: "Source: Bureau of Meteorology (BoM), Climate Data Online — Perth Metro 009225 (1991–2020 normals)"
  - Heritage: "Source: inHerit — State Register of Heritage Places (Heritage Council of WA)"
  - Bushfire: "Source: DFES — Map of Bush Fire Prone Areas (current OBRM designation)"
  - Spatial / aerial: "Source: Landgate Map Viewer Plus / NearMap"
- Place sources at the end of each section or in a footnote — not inline in every sentence

## File Output

- When a skill writes a file, use descriptive filenames: `swanbourne-st-fremantle_planning-envelope.html` not `output.html`. Include the LGA or suburb where relevant.
- Default to markdown (`.md`) for text reports
- Use HTML only for interactive or visual outputs (3D viewers, slide decks, dashboards)
- Include a YAML front matter block in markdown reports with: title, date (Australian format `2026-04-21`), site address / Lot No. / DP No., LGA, skill name

## Lists

- Use bulleted lists for unordered items (materials, features, observations)
- Use numbered lists only for sequential steps or ranked items
- Keep list items parallel in grammar: all start with a verb, or all start with a noun
