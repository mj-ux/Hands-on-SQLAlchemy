from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship

from base import Base


class Member(Base):

    __tablename__ = 'members'

    uid = Column(
        Integer,
        primary_key = True,
    )
    name = Column(
        String,
    )
    famName = Column(
        String,
    )
    organizations = relationship(
        "OrganizationMember",
        back_populates = "members",
    )
