import sys
import json
from datetime import datetime
from zoneinfo import ZoneInfo

timezone = ZoneInfo("Europe/Oslo")

with open('_data/events.json', 'r') as event_file:
    events = json.load(event_file)

# Update the event time for each event to follow timezone in Oslo
for event in events:
    event_time = event['startDate'].replace('Z', '+00:00')
    utc_time = datetime.fromisoformat(event_time)
    oslo_time = utc_time.astimezone(timezone)

    event['startDate'] = oslo_time.isoformat()

with open('_data/events.json', 'w', encoding='utf-8') as event_file:
    json.dump(events, event_file, indent=2, ensure_ascii=False)