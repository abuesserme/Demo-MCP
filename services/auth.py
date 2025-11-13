from fastapi import HTTPException

def check_token(token: str):
    if token != "mock-token":
        raise HTTPException(status_code=401, detail="Invalid or missing token")