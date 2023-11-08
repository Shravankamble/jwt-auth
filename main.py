from fastapi import FastAPI, Request
from app.routers import auth
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

description = """ 
***This Fastapi API Is Use To Create JWT Token for Authorization***.

**There are currently two endpoints in the API which you can use**
            
## Dict
            
*the first endpoint creates a jwt token of any given data in a form of a dict* 
            
## User       
            
*The second endpoint is more like a schema which takes two mandatory paramerters one is email and other one is password
this one is more about Login and stuff (authentication).*
"""

app = FastAPI(
    title="JWT Auth",
    version="v1",
    description=description,
    terms_of_service="https://github.com/Shravankamble/jwt-auth/blob/main/README.md",
    contact={
        "name": "shravan",
        "url": "https://github.com/Shravankamble/jwt-auth/issues/new"
    }
)

app.include_router(auth.router)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
@limiter.limit("100/minute")
async def root(request: Request):
    return "hello jwt auth"
