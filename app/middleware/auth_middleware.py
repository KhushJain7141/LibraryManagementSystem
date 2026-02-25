from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.security import is_token_valid


async def auth_middleware(request: Request, call_next):

    # Allow login + docs without token
    if request.url.path in [
        "/auth/login",
        "/docs",
        "/openapi.json",
        "/redoc",
    ]:
        return await call_next(request)

    token = request.headers.get("Authorization")

    if not token or not is_token_valid(token):
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"},
        )

    request.state.user = {"token": token}
    return await call_next(request)