import sqlalchemy
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID


from dbManagement.base import Base

class User(Base):
    __tablename__ = 'users'
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s')>" % ( 
                self.name, self.fullname)


