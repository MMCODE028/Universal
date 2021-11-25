from datetime import date
from pydantic import BaseModel
from typing import Optional


class Pasajero(BaseModel):
    id: Optional[int]
    nombre: str
    apellido: str
    nacionalidad: str
    fechaDeNacimiento: date
