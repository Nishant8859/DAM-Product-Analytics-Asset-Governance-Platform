"""Create review flags from the synthetic DAM asset inventory.

Run: python clean_and_profile.py
No third-party packages required.
"""
import csv
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "data" / "assets.csv"
OUT = ROOT / "data" / "assets_enriched.csv"
AS_OF = date(2026, 10, 17)  # fixed portfolio snapshot; change deliberately for a new analysis

with SRC.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    exp = date.fromisoformat(row["usage_rights_expiry"]) if row["usage_rights_expiry"] else None
    last_dl = date.fromisoformat(row["last_download_date"]) if row["last_download_date"] else None
    row["low_metadata_flag"] = int(float(row["metadata_completeness_pct"]) < 80)
    row["zero_downloads_90d_flag"] = int(int(row["downloads_90d"]) == 0)
    row["rights_expired_flag"] = int(exp is not None and exp < AS_OF)
    row["rights_expiring_30d_flag"] = int(exp is not None and AS_OF <= exp <= AS_OF + timedelta(days=30))
    row["last_download_age_days"] = (AS_OF - last_dl).days if last_dl else ""
    row["stale_asset_review_flag"] = int(last_dl is None or (AS_OF - last_dl).days > 180)

fieldnames = list(rows[0].keys()) if rows else []
with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Read {len(rows):,} assets; wrote {OUT}")
print(f"Low metadata flags: {sum(int(r['low_metadata_flag']) for r in rows):,}")
print(f"Rights expired flags: {sum(int(r['rights_expired_flag']) for r in rows):,}")
print(f"Rights expiring in 30 days: {sum(int(r['rights_expiring_30d_flag']) for r in rows):,}")
print("Review flags are triage signals; verify with content owners before taking action.")
