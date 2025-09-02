from pydantic import BaseModel, Field


class TokenInfo(BaseModel):

    uuid: str
    name: str
    exp: float


class Login(BaseModel):

    login: str
    password: str


class User(BaseModel):

    name: str = Field(min_length=2, max_length=12)
    login: str = Field(min_length=6, max_length=20)
    password: str = Field(min_length=6, max_length=20)