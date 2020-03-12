from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship

from models.organization import Organization
from models.member import Member
from models.organizationMember import OrganizationMember
import base


engine = create_engine(
    'sqlite:///maestro.sqlite',
    echo = True,
)
base.Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
organizations = []
for i in range(10):
    organization = Organization(
        org_name = 'org' + str(i),
    )
    organizations.append(organization)
members = []
for i in range(20):
    member = Member(
        name = 'user' + str(i),
        famName = 'famName' + str(i),
    )
    member.organizations.append(
        OrganizationMember(organizations=organizations[i%10]),
    )
    session.add(member)
    session.commit()
