import sys
import json
from datetime import datetime
from zoneinfo import ZoneInfo

daylight_start = datetime.fromisoformat(sys.argv[1])
daylight_end = datetime.fromisoformat(sys.argv[2])
timezone = ZoneInfo(sys.argv[3])

with open('_data/events.json', 'r') as event_file:
    events = json.load(event_file)

for event in events:
    event_time = event['startDate'].replace('Z', '+00:00')
    utc_time = datetime.fromisoformat(event_time)
    oslo_time = utc_time.astimezone(timezone)

    event['startDate'] = oslo_time.isoformat()

with open('_data/events.json', 'w', encoding='utf-8') as event_file:
    json.dump(events, event_file, indent=2, ensure_ascii=False)