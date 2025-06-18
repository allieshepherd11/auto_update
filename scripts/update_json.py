import json
from datetime import datetime

# Load the existing file
with open("data/data.json", "r") as f:
    data = json.load(f)

# Make sure the structure exists
if "title" not in data:
    data["title"] = "GitHub Actions Test Log"
if "tests" not in data:
    data["tests"] = []

# Add a new test entry
test_number = len(data["tests"]) + 1
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
data["tests"].append(f"Test {test_number} — {timestamp}")

# Save the updated file
with open("data/data.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Appended Test {test_number}")
