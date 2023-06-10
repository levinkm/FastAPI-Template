from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings
from pymongo import MongoClient

#+++++++++++++++++++++++++++++++++++ Postgresql +++++++++++++++++++++++++++++++++++++++++++++


# connect to the postgresql database and create a session
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

Engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=Engine, autocommit=False, autoflush=False)

DB = Session()

Base = declarative_base()


# dependancy
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


#+++++++++++++++++++++++++++++++++++++++++++ MongoDB +++++++++++++++++++++++++++++++++++++++++++


# Create MongoDB client
client = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)

# Access the database
mongodb = client[settings.MONGO_DB]




