# Data dictionary

The cleaned dataset contains one row per post in one collected RSS snapshot.

| Field | Type | Meaning |
|---|---|---|
| `post_url` | text | Public URL of the featured blog post. |
| `published_at_utc` | ISO 8601 timestamp | Publication timestamp supplied by the RSS feed, converted to UTC. |
| `collected_at_utc` | ISO 8601 timestamp | UTC time when the RSS feed snapshot was retrieved. |
| `age_hours` | decimal number | Difference between collection time and publication time, measured in hours. |

Rows without a usable post URL or publication timestamp are excluded. Entries with a negative calculated age are also excluded because their publication time is later than the collection time. The sample CSV contains at most the first 10 cleaned rows from the latest snapshot.
