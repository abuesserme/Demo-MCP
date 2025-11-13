from services.auth import check_token
from services.accounts import search_accounts_service

def search_accounts_handler(q: str, Authorization: str = None):
    check_token(Authorization)
    return search_accounts_service(q)