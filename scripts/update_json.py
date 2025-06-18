# scripts/update_json.py
import json
from datetime import datetime

data = {
    "updated_at": datetime.utcnow().isoformat(),
    "message": "This is a test update!"
}

with open("data/data.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ data.json updated.")
