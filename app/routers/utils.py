import os
from dotenv import load_dotenv
from jose import jwt, jwe
from datetime import datetime, timedelta
from schemas import User, Login

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

TOKEN_EXPIRE_TIME = 60

def create_access_token(data: dict, exp_time: int = 0):
    to_encode = data.copy()
    
    current_time = datetime.utcnow()
    
    if exp_time: 
        expire_time = datetime.utcnow() + timedelta(minutes=(TOKEN_EXPIRE_TIME + int(exp_time)))
    else: 
        expire_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_TIME)
        
    to_encode.update({"iat": current_time})
    
    to_encode.update({"exp": expire_time})
    
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded

def create_user_token(data: User, expire: int = 0):
    user_token = create_access_token(data=data, exp_time=expire)
    return user_token

