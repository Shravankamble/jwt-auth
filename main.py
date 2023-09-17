from fastapi import FastAPI, status, Request
from app.routers import auth

description = """ 
***This Fastapi API Is Use To Create JWT Token for Authorization***.

**There are currently two endpoints in the API which you can use**
            
## Dict
            
*the first endpoint creates a jwt token of any given data in a form of a dict* 
            
## User       
            
*The second endpoint is more like a schema which takes two mandatory paramerters one is eamil and other one is password
this one is more about Login and stuff (authentication).*
"""

app = FastAPI(
    title="JWT Auth",
    version="v0.1",
    description=description,
    terms_of_service="https://github.com/Shravankamble/jwt-auth/blob/main/README.md",
    contact={
        "name": "shravan",
        "url": "https://github.com/Shravankamble/jwt-auth/issues/new"
    }
)

app.include_router(auth.router)

@app.get("/")
async def root():
    return "hello jwt auth"

