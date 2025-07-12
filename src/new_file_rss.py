import json
import importlib.util
from pathlib import Path

# 1) Load your config.py
config_path = Path("config.py")
spec = importlib.util.spec_from_file_location("config", str(config_path))
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)
rss_feeds = config.rss_feeds

# 2) Define the field order you care about
FIELD_ORDER = ["url", "country", "source", "category"]

# 3) Group feeds by country
grouped = {}
for feed in rss_feeds:
    country = feed.get("country") or "general"
    grouped.setdefault(country, []).append(feed)

# 4) Export one JSON per country, rebuilding each feed dict in FIELD_ORDER
out_dir = Path("rss_configs")
out_dir.mkdir(exist_ok=True)

for country, feeds in grouped.items():
    filename = "general_rss.json" if country == "general" else f"{country.lower().replace(' ', '_')}.json"
    path = out_dir / filename

    # Rebuild list with ordered keys
    ordered_list = [
        { key: feed.get(key) for key in FIELD_ORDER if key in feed }
        for feed in feeds
    ]

    with open(path, "w") as f:
        json.dump(ordered_list, f, indent=2)
    print(f"Wrote {len(feeds)} feeds to {path}")
