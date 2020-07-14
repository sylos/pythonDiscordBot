import uuid
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import BigInteger, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from dbManagement.base import Base

class DBGuildMember(Base):
    __tablename__ = "guild_members"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), primary_key=True)
    guild_id = Column(BigInteger, ForeignKey('guilds.id'), primary_key=True)
    present = Column(Boolean)
    user = relationship('User', lazy="joined", back_populates='guilds')
    guild = relationship('DBGuild', lazy="joined", back_populates='members')

    def __repr__(self):
        return "DBGuildMembers id='%s', user_id='%s', guild_id='%s', present='%s'" % (
                self.id, self.user_id, self.guild_id, self.present)
