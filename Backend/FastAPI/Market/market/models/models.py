from pydantic import BaseModel


class ItemInfo(BaseModel):

    name: str
    weight: int
    price: int