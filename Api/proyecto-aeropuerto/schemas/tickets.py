from datetime import date
from pydantic import BaseModel
from typing import Optional


class Tickets(BaseModel):
    id: Optional[str]
    idPasajero: int
    idVuelo: str
