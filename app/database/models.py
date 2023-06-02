from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    Float,
)


Base = declarative_base()


class Temperature(Base):
    __tablename__ = "temperature"
    id = Column(Integer, primary_key=True, index=True)
    temperature_dht = Column(Float)
    humidity_dht = Column(Float)
    temperature_ext = Column(Float)
    temperature_int = Column(Float)
    temperature_bmp = Column(Float)
    airpreassure = Column(Float)
    ligth_infrared = Column(Float)
    ligth_lux = Column(Float)
