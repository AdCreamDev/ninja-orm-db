from SQLAlchemy import create_engine, Column, Integer, String
from SQLAlchemy.orm import sessionmaker
from SQLAlchemy.ext.declarative import declarative_base

import dotenv
import os

Base = declarative_base()

class TESTDB(Base):
    __tablename__ = 'test1'
    seq = Column(Integer, primary_key=True)
    num = Column(Integer)
    data = Column(String(255))

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

engine = create_engine(os.environ["SQL_URL"])

Session  = sessionmaker(bind=engine)
session = Session()

# Dependency
users = session.query(TESTDB).all()
for user in users:
    print(user.num, user.data)
