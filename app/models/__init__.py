from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .. import db


class Test(db.Model):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
