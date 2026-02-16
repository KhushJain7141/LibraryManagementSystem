import base64
from fastapi import Request
from fastapi.responses import JSONResponse


# Hardcoded credentials (for now) 
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"


def validate_credentials(request: Request):
    """
    Validate Basic Auth credentials.
    Returns user dict if valid, else None.
    """
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    try:
        scheme, credentials = auth_header.split()

        if scheme.lower() != "basic":
            return None

        decoded = base64.b64decode(credentials).decode("utf-8")
        username, password = decoded.split(":")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return {"username": username, "role": "admin"}

    except Exception:
        return None

    return None


async def auth_middleware(request: Request, call_next):
    user = validate_credentials(request)

    if not user:
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"},
        )

    request.state.user = user

    response = await call_next(request)
    return response
