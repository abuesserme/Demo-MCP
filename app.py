from fastapi import FastAPI, Header
from tools.search_accounts import search_accounts_handler
from tools.get_account_details import get_account_details_handler

app = FastAPI()

@app.get("/")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "demo_mcp_connector"}

@app.get("/search_accounts")
def search_accounts(q: str, authorization: str = Header(None)):
    return search_accounts_handler(q=q, Authorization=authorization)

@app.get("/get_account_details/{account_id}")
def get_account_details(account_id: int, authorization: str = Header(None)):
    return get_account_details_handler(account_id=account_id, Authorization=authorization)