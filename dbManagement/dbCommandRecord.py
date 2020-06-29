from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from discord import Message
from sqlalchemy import Column, Integer, String

from dbManagement.base import Base


class DBCommandRecord(Base):
    __tablename__ = 'command_record'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    author = Column(String)
    content = Column(String)
    channel = Column(String)
    guild = Column(String)
    messages_id = Column(Integer)

    def __repr__(self):
        "<Message(author='%s', content='%s')>" % (self.author, self.content)


