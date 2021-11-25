from pydantic import BaseModel
from typing import Optional


class Aeropuertos(BaseModel):
    id: Optional[str]
    nombre: str
    ciudad: str
