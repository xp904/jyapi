# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AppUser(Base):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    auth_string = Column(String(100))
    email = Column(String(50))

