from pydantic import BaseModel
from typing import Optional
from datetime import date


class Salidas(BaseModel):
    id: Optional[str]
    idAeropuerto: str
    fecha: date