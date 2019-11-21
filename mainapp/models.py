# coding: utf-8
from sqlalchemy import Column, Integer, String, Float, Text, FetchedValue
from sqlalchemy.ext.declarative import declarative_base

import db

Base = declarative_base()
metadata = Base.metadata


class AppUser(Base):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    auth_string = Column(String(100))
    email = Column(String(50))


class TCategory(Base):
    __tablename__ = 't_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    ord_sn = Column(Integer)
    parent_id = Column(Integer, server_default=FetchedValue(), default=0)

    @property
    def parent(self):
        if self.parent_id != 0:
            return db.session.query(TCategory).filter(TCategory.id == self.parent_id).first()

    @property
    def childens(self):
        return db.session.query(TCategory).filter_by(parent_id=self.id).all()


class TProduct(Base):
    __tablename__ = 't_product'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    cover = Column(String(200))
    price = Column(Float)
    summary = Column(Text)
    category_id = Column(Integer)
