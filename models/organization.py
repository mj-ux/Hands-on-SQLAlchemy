from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship

from base import Base


class Organization(Base):
    __tablename__ = 'organizations'
    id = Column(
        Integer,
        primary_key = True,
    )
    org_name = Column(
        String,
    )
    members = relationship(
        "OrganizationMember",
        back_populates = "organizations",
    )
