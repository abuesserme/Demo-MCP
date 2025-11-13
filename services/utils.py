import json

def load_data():
    with open("mock_data.json", "r") as f:
        return json.load(f)

def simplify_account(acc):
    return {
        "id": acc["id"],
        "name": acc["name"],
        "type": acc["type"],
        "location": acc["location"]
    }