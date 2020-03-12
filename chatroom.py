from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

import base
from models.room import Room
from models.message import Message

engine = create_engine(
    'sqlite:///chatroom.sqlite',
    echo = True,
)
base.Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
rooms = []
for i in range(0, 10):
    newRoom = Room()
    rooms.append(newRoom)
for i in range(0, 10):
    newMessage = Message(
        body = "salam" + str(i),
    )
    rooms[i].messages.append(newMessage)
    session.add(newMessage)
rooms[1].messages[-1].body="shiiiiiiiiiit"
session.commit()
print(rooms[1].last_message)
