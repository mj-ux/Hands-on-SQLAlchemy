from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship

from base import Base


class OrganizationMember(Base):

    __tablename__ = 'organization_member'

    organization_id = Column(
        Integer,
        ForeignKey('organizations.id'),
        primary_key = True,
    )
    member_id = Column(
        Integer,
        ForeignKey('members.uid'),
        primary_key = True,
    )
    organizations = relationship(
        "Organization",
        back_populates = "members",
    )
    members = relationship(
        "Member",
        back_populates = "organizations",
    )
