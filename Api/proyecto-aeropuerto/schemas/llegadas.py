from pydantic import BaseModel
from typing import Optional
from datetime import date


class Llegadas(BaseModel):
    id: Optional[str]
    idAeropuerto: str
    fecha: date