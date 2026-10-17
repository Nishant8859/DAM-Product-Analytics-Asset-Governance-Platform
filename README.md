# Project 1 — DAM Product Analytics & Asset Governance Platform

## Portfolio summary
A simulated enterprise digital asset management (DAM) analytics solution that brings asset inventory, usage events, metadata completeness, rights dates, and workflow aging into a decision-ready product dashboard.

**Target roles:** Product Analyst, Associate Product Manager, Technical Product Manager, Product Operations Analyst.

**Tools:** Power BI, SQL (SQLite-compatible starter queries), Python, CSV/API concepts, product analytics.

**Important:** All included records are synthetic and were created for portfolio practice. They are not company data and should not be represented as Valvoline or Acquia production results.

## Business problem
Brand, marketing, and sales teams need to answer: Which assets create value? Which are difficult to discover? Which assets present rights/compliance risk? Where do approval workflows stall? Without connected reporting, these questions often require manual exports and ad hoc analysis.

## What to build
1. Import `data/assets.csv`, `data/usage_events.csv`, and `data/workflow_tasks.csv` into Power BI or SQLite.
2. Validate joins, date formats, uniqueness, null rates, and row counts. `asset_id` is the asset key; usage events and workflow tasks are many-to-one with assets.
3. Use the SQL in `sql/analysis_queries.sql` to answer the core questions.
4. Build a 3-page Power BI report using `powerbi/dashboard_spec.md` and measures in `powerbi/dax_measures.dax`.
5. Write a short product decision memo: the top three actions you would prioritize based on the dashboard, the evidence supporting each, and how you would measure impact.
6. Optional stretch: replace the synthetic tables with an authorized Acquia DAM API extract. Never embed an API token in a PBIX, GitHub repository, or shared document. Use an approved credential store/parameter approach and follow your employer's security rules.

## Key product questions
- What percentage of assets have complete metadata?
- What share of assets received no downloads in the last 90 days?
- How many approved assets have rights expiring in the next 30 days?
- Which asset types, regions, or teams have lower utilization?
- Which workflow stages have the longest open-task aging?
- What action should the product team take first, and what trade-off does it involve?

## Success metrics (targets are hypotheses, not achieved results)
- Increase metadata completeness by 10 percentage points in a controlled pilot.
- Reduce the share of eligible assets with zero downloads over 90 days by 10% relative to baseline.
- Reduce median open-workflow age by 15% in the pilot workflow.
- Reach at least 90% weekly active usage among the pilot's intended report users after rollout.

## Deliverables for a credible portfolio
- Power BI `.pbix` file or clear screenshots of report pages.
- Data model diagram and a one-page metric dictionary.
- SQL file with analysis queries and validation checks.
- A 1-page product recommendation memo describing what should be built next and why.
- A README that states dataset is synthetic and records what you personally implemented.

## Suggested analysis narrative
Avoid declaring that low downloads automatically mean an asset is useless. Separate evergreen/reference content from campaign content, account for recency and rights, and validate findings with users. Recommendations should be based on evidence, not just rankings.
