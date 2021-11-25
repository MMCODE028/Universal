from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import DATE, Integer, String

aviones = Table("aviones", meta, Column("id", String(255), primary_key=True),
                Column("nombre", String(255)), Column("idModelo", String(255)),
                Column("idAerolinea", String(255)),
                Column("aforoTotal", Integer))

meta.create_all(engine)
