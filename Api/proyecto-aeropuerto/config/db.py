from sqlalchemy import create_engine, MetaData

engine = create_engine(
    "mysql+pymysql://root:misiontic@localhost:3306/aeropuerto")
meta = MetaData()
conn = engine.connect()