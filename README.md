# How Recent Are the Posts Featured in Bear Blog’s Trending Feed?

**Mia Rosner**  
**INFO 4617 — Final Project**

This project investigates how recent the posts featured in Bear Blog’s trending feed are. I plan to collect the public Discovery RSS feed once daily at 8:00 p.m. Mountain Time for 14 consecutive days, calculate the age of each featured post, and examine how the feed’s post-age distribution changes over the study period.

## Data
Source: [Bear Blog Discovery RSS feed](https://bearblog.dev/discover/feed/). Daily observations will be saved in `data/`. Planned fields: post URL, publication timestamp, collection timestamp, and calculated age in hours.

## Methods
Python: `requests` and `feedparser` for collection and parsing, `pandas` for organizing and analyzing observations, and `matplotlib` for visualizations.

## Findings
*To be completed after data collection and analysis.*

## How to reproduce
1. Install `requests`, `feedparser`, `pandas`, and `matplotlib`.
2. Open `notebook.ipynb` in Jupyter.
3. Run the collection cell once at each scheduled collection time.
4. Run the analysis cells after collecting the data.

*This repository is a project-in-progress. The study has not yet been conducted.*
