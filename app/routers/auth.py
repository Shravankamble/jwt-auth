from fastapi import APIRouter, status, Depends
from fastapi.responses import Response
from app.routers.utils import create_access_token, create_user_token
from schemas import User

router = APIRouter(
    tags=["auth"]
)


@router.get("/auth")
async def hello_auth():
    return "This Web Server Is Used To Create JWT Token For Authentication Purposes!!"
    
@router.post("/api/v1/jwt/dict")
def jwt_dict(data: dict, expiration_in_minutes: int = 0):
    exp_token_time = f"You Can Use The Above Token For {(60 + expiration_in_minutes)} Minutes!" 
    jwt_token = create_access_token(data=data, exp_time=expiration_in_minutes)
    return {"Token": jwt_token, "response": Response(exp_token_time, status_code=status.HTTP_200_OK)}

@router.post("/api/v1/jwt/user", status_code=status.HTTP_200_OK)
def jwt_user(data: User, exp_time: int = 0):
    exp_token_time = f"You Can Use The Above Token For {(60 + exp_time)} Minutes!"  
    user_token = create_user_token(data={"email": data.email, "password": data.password}, expire=exp_time)
    return {"Token": user_token, "response": Response(exp_token_time, status_code=status.HTTP_200_OK)}