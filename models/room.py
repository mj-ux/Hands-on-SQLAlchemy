from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship, column_property
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import select

from base import Base
from models.message import Message


class Room(Base):

    __tablename__ = 'rooms'

    id = Column(
        Integer,
        primary_key = True,
    )
    messages = relationship(
        "Message",
        backref = "rooms",
    )
    #last_message = column_property(select([Message.id, Message.body]))
    last_message = column_property(
        select(
            [Message.body]
        ).
	where(
            Message.roomId==id
	).
        order_by(
            Message.id.desc()
        ).
        limit(1)
    )

#SELECT * FROM monsters WHERE uid IN (SELECT uid FROM added_monsters)
