from pydantic import BaseModel
from typing import Optional


class Aerolineas(BaseModel):
    id: Optional[str]
    nombre: str
