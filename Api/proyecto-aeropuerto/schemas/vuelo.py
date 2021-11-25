from pydantic import BaseModel
from typing import Optional
from datetime import date


class Vuelos(BaseModel):
    id: Optional[str]
    idLlegada: str
    idSalida: str
    idAvion: str