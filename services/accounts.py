from .utils import load_data, simplify_account
from fastapi import HTTPException

db = load_data()

def search_accounts_service(query: str):
    query = query.lower()
    results = []

    for acc in db["accounts"]:
        if query in acc["name"].lower():
            results.append(simplify_account(acc))

    return {
        "results": results,
        "summary": f"Found {len(results)} accounts matching '{query}'."
    }


def get_account_details_service(account_id: int):
    for acc in db["accounts"]:
        if acc["id"] == account_id:
            return {
                "id": acc["id"],
                "name": acc["name"],
                "type": acc["type"],
                "location": acc["location"],
                "primary_contact": acc["contact"],
                "summary": f"{acc['name']} is a {acc['type']} firm located in {acc['location']}."
            }

    raise HTTPException(status_code=404, detail="Account not found")