from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import DATE, Integer, String

salidas = Table("salidas", meta, Column("id", String(255), primary_key=True),
                Column("idAeropuerto", String(255)), Column("fecha", DATE))

meta.create_all(engine)
