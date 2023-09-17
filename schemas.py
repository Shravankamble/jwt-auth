from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    password: str
    DESCRIPTION: Optional[str] = "This is for user authentication such as users email and password you can add your own ↙"
    GITHUB: Optional[str] = "https://github.com/Shravankamble/auth-api.git"
    