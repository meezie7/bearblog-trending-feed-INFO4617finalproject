"""Clean a locally saved Bear Blog RSS snapshot into a tidy CSV sample."""
from datetime import datetime, timezone
from pathlib import Path
import json

import feedparser
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
DATA_DIR = PROJECT_DIR / "data"
SAMPLE_PATH = DATA_DIR / "cleaned_sample.csv"
FULL_PATH = RAW_DIR / "cleaned_full_local.csv"

def main():
    raw_files = sorted(RAW_DIR.glob("bearblog_raw_*.xml"))
    if not raw_files:
        raise FileNotFoundError(
            "No raw XML found. Run collect.py first to retrieve the RSS feed."
        )

    raw_path = raw_files[-1]
    matching_metadata = sorted(RAW_DIR.glob("bearblog_metadata_*.json"))
    metadata = json.loads(matching_metadata[-1].read_text(encoding="utf-8"))

    feed = feedparser.parse(raw_path.read_bytes())
    collected_at = pd.to_datetime(metadata["collected_at_utc"], utc=True)

    rows = []
    skipped_missing_date = 0
    skipped_missing_url = 0
    skipped_invalid_age = 0

    for entry in feed.entries:
        link = entry.get("link")
        published = entry.get("published_parsed") or entry.get("updated_parsed")

        if not link:
            skipped_missing_url += 1
            continue
        if published is None:
            skipped_missing_date += 1
            continue

        published_at = datetime(*published[:6], tzinfo=timezone.utc)
        published_ts = pd.Timestamp(published_at)
        age_hours = (collected_at - published_ts).total_seconds() / 3600

        if age_hours < 0:
            skipped_invalid_age += 1
            continue

        rows.append({
            "post_url": link.strip(),
            "published_at_utc": published_ts.isoformat(),
            "collected_at_utc": collected_at.isoformat(),
            "age_hours": round(age_hours, 3),
        })

    columns = [
        "post_url", "published_at_utc", "collected_at_utc", "age_hours"
    ]
    cleaned = pd.DataFrame(rows, columns=columns)
    if not cleaned.empty:
        cleaned = cleaned.sort_values("age_hours").reset_index(drop=True)

    # Full cleaned data stays local; only a small sample is intended for Git.
    cleaned.to_csv(FULL_PATH, index=False)
    cleaned.head(10).to_csv(SAMPLE_PATH, index=False)

    print(f"Raw feed file: {raw_path.name}")
    print(f"Entries in feed: {len(feed.entries)}")
    print(f"Clean records: {len(cleaned)}")
    print(f"Skipped (missing publication date): {skipped_missing_date}")
    print(f"Skipped (missing URL): {skipped_missing_url}")
    print(f"Skipped (negative age): {skipped_invalid_age}")
    print(f"Full cleaned data saved locally: {FULL_PATH.relative_to(PROJECT_DIR)}")
    print(f"Public sample saved: {SAMPLE_PATH.relative_to(PROJECT_DIR)}")
    print("\nCleaned sample preview:")
    print(cleaned.head(10).to_string(index=False))

if __name__ == "__main__":
    main()
