from pydantic import BaseModel
from typing import Optional


class Aviones(BaseModel):
    id: Optional[str]
    nombre: str
    idModelo: str
    idAerolinea: str
    aforoTotal: int