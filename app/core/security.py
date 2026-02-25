import secrets

VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

active_tokens = set()


def authenticate_user(username: str, password: str):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return {"username": username, "role": "admin"}
    return None


def create_token():
    return secrets.token_hex(16)


def add_token(token: str):
    active_tokens.add(token)


def is_token_valid(token: str):
    return token in active_tokens