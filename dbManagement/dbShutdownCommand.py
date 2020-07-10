import uuid
from dbManagement.base import Base
from sqlalchemy import BigInteger, Boolean, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from dbManagement.base import Base

class DBShutdownCommand(Base):
    __tablename__ = 'shutdown_commands'

    id = Column(BigInteger, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    author_id = Column(BigInteger)
    shutdown_at = Column(DateTime)
    channel_id = Column(BigInteger)
    restart = Column(Boolean)
