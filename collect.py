"""Collect one snapshot of the Bear Blog Discovery RSS feed.

Run once per scheduled collection (planned: 8:00 p.m. America/Denver).
Raw XML is saved locally under data/raw/ and is excluded from Git.
"""
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
import json
import time

import requests

FEED_URL = "https://bearblog.dev/discover/feed/"
PROJECT_DIR = Path(__file__).resolve().parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = (
    "INFO4617-BearBlog-Research/1.0 "
    "(student research project collecting one public RSS snapshot per day)"
)

def main():
    collected_local = datetime.now(ZoneInfo("America/Denver"))
    collected_utc = collected_local.astimezone(timezone.utc)
    stamp = collected_local.strftime("%Y%m%d_%H%M%S_%Z")

    headers = {"User-Agent": USER_AGENT}
    response = requests.get(FEED_URL, headers=headers, timeout=20)
    try:
        response.raise_for_status()
        raw_path = RAW_DIR / f"bearblog_raw_{stamp}.xml"
        raw_path.write_bytes(response.content)

        metadata = {
            "source": FEED_URL,
            "collected_at_local": collected_local.isoformat(),
            "collected_at_utc": collected_utc.isoformat(),
            "http_status": response.status_code,
            "user_agent": USER_AGENT,
            "raw_file": str(raw_path.relative_to(PROJECT_DIR)),
        }
        metadata_path = RAW_DIR / f"bearblog_metadata_{stamp}.json"
        metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

        print(f"HTTP status: {response.status_code}")
        print(f"Raw feed saved locally: {raw_path.relative_to(PROJECT_DIR)}")
        print(f"Collection time (Mountain): {collected_local.isoformat()}")
        print("The raw XML is intentionally excluded from the public repository.")
    finally:
        # One request per run; pause before any subsequent request.
        time.sleep(2)

if __name__ == "__main__":
    main()
