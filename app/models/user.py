from typing import Any
from pydantic import BaseModel


class AddToCartModel(BaseModel):
    item_id: str
    user_id: str
