from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://avnadmin:AVNS_oFkWvN519mb41sJfsyG@mysql-1aed615a-proyetointegradora-2c1d.e.aivencloud.com:20518/defaultdb'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@localhost:3307/test'  #Conexión local

#  Conexión local
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
