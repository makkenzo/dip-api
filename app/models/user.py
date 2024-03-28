from typing import Any
from pydantic import BaseModel


class AddToCartModel(BaseModel):
    uid: str
