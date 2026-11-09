# How Recent Are the Posts Featured in Bear Blog's Trending Feed?

**Mia Rosner**  
INFO 4617 — Final Project

This project investigates how recent the posts featured in Bear Blog's trending feed are. I plan to collect the public Discovery RSS feed, calculate the age of each featured post, and examine how the feed's post-age distribution changes over time.

## Data

**Source:** [Bear Blog Discovery RSS feed](https://bearblog.dev/discover/feed/).

**Collection method:** A Python script using `requests` retrieves one public RSS snapshot with an identifying User-Agent and a 20-second timeout.

**Test collection:** November 8, 2026, at 7:39 p.m. Mountain Time.

**Test results:** HTTP 200; 20 RSS entries retrieved and 20 successfully cleaned.

**Cleaning:** The RSS feed was parsed using `feedparser` and organized with `pandas`. The cleaned dataset includes post URLs, publication timestamps, collection timestamps, and calculated age in hours.

**Public sample:** `data/cleaned_sample.csv` contains 10 records from the test snapshot. See `data/data_dictionary.md` for field definitions.

**Not included:** The complete raw RSS XML and full cleaned dataset are stored locally and excluded from the public repository through `.gitignore`. This avoids redistributing the entire feed and sharing more individual post links than necessary.

**Study status:** This is a preliminary one-time test of the collection and cleaning workflow, not the completed 14-day study described in the proposal.

## Methods

Python collection and cleaning scripts using `requests`, `feedparser`, and `pandas`. The collection script retrieves the RSS feed; the cleaning script extracts timestamps, calculates post age, and produces a tidy CSV.

## Findings

Preliminary test: 20 records were successfully cleaned. The full study and analysis have not yet been completed.

## How to reproduce

1. Install dependencies with `python3 -m pip install -r requirements.txt`.
2. Run `python3 collect.py` to retrieve and save one raw RSS snapshot locally.
3. Run `python3 clean.py` to clean the latest snapshot and generate the sample CSV.