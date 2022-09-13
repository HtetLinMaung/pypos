from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: str


class UserCreate(UserBase):
    password: str
    name: str
    pass


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: str
    name: str
    profile_image: str
    created_by: str
    created_at: str
    updated_at: str
    deleted_at: str

    class Config:
        orm_mode = True
