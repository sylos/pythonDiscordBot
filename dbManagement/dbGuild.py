import sqlalchemy
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


from dbManagement.base import Base

class DBGuild(Base):
    __tablename__ = 'guilds'

    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    id = Column(Integer, primary_key=True)
    guild_id = Column(BigInteger, unique=True)
    members = relationship('DBGuildMember', back_populates='guild')
        
    def __repr__(self):
        return "DBGuild: id='%s', guild_id='%s'" % (self.id, self.guild_id)
    #guildname
    #memberlist
    #guildimage


