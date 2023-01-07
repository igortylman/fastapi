from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserCreatedResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: str
    created_at: datetime
    user_id: int
    post_owner: UserCreatedResponse
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]

class Vote(BaseModel):
    post_id: int
    vote_dir: conint(le=1)


