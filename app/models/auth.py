from typing import Any
from pydantic import BaseModel


class RegistrationModel(BaseModel):
    data: Any
    object: str
    type: str

    class Config:
        allow_population_by_field_name = True
