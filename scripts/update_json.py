import json
from datetime import datetime

# Load existing data
try:
    with open("data/data.json", "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {"title": "GitHub Actions Test Log", "tests": []}

# Ensure keys exist
if "title" not in data:
    data["title"] = "GitHub Actions Test Log"
if "tests" not in data:
    data["tests"] = []

# Add new test entry
test_num = len(data["tests"]) + 1
timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
data["tests"].append(f"Test {test_num} — {timestamp}")

print(f"Tests before: {len(data['tests'])}")

# Save updated JSON
with open("data/data.json", "w") as f:
    json.dump(data, f, indent=2)


print(f"✅ Test {test_num} added at {timestamp}")
print(f"Tests after: {len(data['tests'])}")