from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import DATE, Integer, String

tickets = Table("tickets", meta, Column("id", Integer, primary_key=True),
                Column("idPasajero", Integer), Column("idVuelo", String(255)))

meta.create_all(engine)