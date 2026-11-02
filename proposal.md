# INFO 4617 — Final Project Proposal

**Mia Rosner**  
**October 25, 2026**

# Bear Blog: How Recent Are the Posts Featured in the Trending Feed?

## 1. Research Question

- **Research question:** How recent are the posts featured in Bear Blog’s trending feed?
- **Purpose:** Today, the internet is often associated with algorithms, homepages, and never-ending feeds. Independent blogging interests me because it requires users to actively seek out what they want to read. Different platforms prioritize content differently, and their discovery features reflect those choices. I want to investigate whether Bear Blog’s trending feed primarily features posts published within the last few hours or also includes posts that are a day or several days old.
- **Audience:** Data researchers, Bear Blog users, independent bloggers, writers, and digital archivists interested in how online content is surfaced.
- **Expected result and surprise:** I expect the feed to contain a range of post ages, with many posts published within the previous 24 hours. I would be surprised if nearly all featured posts were only a few hours old. The study will test these expectations using repeated observations rather than a single snapshot.

## 2. Data Sources and Methods

- **Sources:** Bear Blog Discovery page: https://bearblog.dev/discover/ ; RSS feed: https://bearblog.dev/discover/feed/
- **How I will collect the data:** I will use Python’s `requests` library to retrieve the RSS feed, `feedparser` to parse its entries, and `pandas` to organize the data. I will use Matplotlib to visualize the results. This method draws on course materials about web data collection, structured feeds, and automated collection.
- **Collection schedule and scope:** I will collect the feed once daily at **8:00 p.m. Mountain Time for 14 consecutive days**. Each collection will record the collection timestamp and all available feed entries, including each post’s title, URL, publication timestamp, and calculated age in hours. I will save each daily collection to a CSV file so observations can be combined and analyzed reproducibly. This will create a longitudinal dataset showing how the feed’s post-age distribution changes across two weeks. Because the same post may appear on multiple days, I will retain each daily observation to track how its age changes over time and use post URLs to identify repeated entries.
- **Analysis:** Using Python, I will calculate the median and mean age of featured posts for each day, the youngest and oldest post ages, and the percentage of entries published within the previous 12, 24, and 48 hours. I will create a histogram to show the overall distribution of post ages and a line chart to compare the daily median age across the study period. I will interpret the findings descriptively rather than assume that post age explains why a post appears in the feed.

## 3. Ethics and Feasibility

- **Terms of Service and `robots.txt`:** I reviewed Bear Blog’s [Terms of Service](https://docs.bearblog.dev/terms-of-service/) and [Code of Conduct](https://docs.bearblog.dev/code-of-conduct/). I also checked https://bearblog.dev/robots.txt, which returned HTTP 404, so I could not verify crawling directives at that URL. A missing file does not establish permission to scrape, and I have not identified a specific fair-use or research exception that overrides the platform’s rules. I will limit collection to one request per day, use a descriptive User-Agent, set request timeouts, and stop if access is denied or the platform’s policies do not permit collection.
- **Personal information:** The feed includes blog titles and links to individual posts, which may reveal authors’ identities or personal interests. I will collect only the fields needed for the research question: post URL, publication timestamp, collection timestamp, and calculated age in hours. I will use aggregate statistics and visualizations, avoid analyzing authors’ identities or post content, and avoid reproducing titles or other personal details unnecessarily.
- **One record, retrieved:** My preliminary request to the RSS feed returned HTTP 200 with an XML response. I parsed the feed using `feedparser` and retrieved this example entry:
  - **Request URL:** https://bearblog.dev/discover/feed/
  - **Status code:** `200`
  - **Title:** “I won’t let my husband see my blog”
  - **Publication timestamp:** `2026-10-24T22:34:00+00:00`
  - **Post URL:** https://littleducky.bearblog.dev/i-wont-let-my-husband-see-my-blog/
  - **Fields I will use:** post URL, publication timestamp, collection timestamp, and calculated age in hours. The title may be retained temporarily to inspect parsed data but is not needed for the analysis.
- **Biggest risk and fallback:** The feed may change, become unavailable, or contain entries without valid publication timestamps. I will save each successful daily collection to a separate CSV file, record failed requests, and exclude entries with invalid timestamps from age calculations while documenting missing data. If collecting for the full two weeks is not feasible or permitted, I will analyze the observations collected successfully and clearly state the shorter study period and its limitations.

## AI Tools Disclosure
I used ChatGPT to refine the research question, plan the collection schedule, and organize the proposal around the rubric. I conducted a preliminary retrieval test and will implement and verify the collection and analysis code as part of the project.
