from pydantic import BaseModel
from typing import Optional
from datetime import date


class Modelos(BaseModel):
    id: Optional[str]
    nombre: str
    marca: str