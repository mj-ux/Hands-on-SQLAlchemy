from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship

from base import Base


class Message(Base):

    __tablename__ = 'message'

    id = Column(
        Integer,
        primary_key = True,
    )
    roomId = Column(
        Integer,
        ForeignKey('rooms.id'),
    )
    body = Column(
        String,
    )
