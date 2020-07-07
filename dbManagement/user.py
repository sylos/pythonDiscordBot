import sqlalchemy
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger
from sqlalchemy.dialects.postgresql import UUID


from dbManagement.base import Base

class User(Base):
    __tablename__ = 'users'
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    id = Column(Integer, primary_key=True)
    unique_user_id = Column(BigInteger, unique=True)
    
    def __repr__(self):
        return "<User(u_user_id='%s')>" % ( 
                self.unique_user_id)


