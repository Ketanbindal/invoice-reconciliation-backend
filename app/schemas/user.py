from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
