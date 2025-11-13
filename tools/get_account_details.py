from services.auth import check_token
from services.accounts import get_account_details_service

def get_account_details_handler(account_id: int, Authorization: str = None):
    check_token(Authorization)
    return get_account_details_service(account_id)