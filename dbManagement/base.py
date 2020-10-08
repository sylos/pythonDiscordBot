from sqlalchemy.ext.declarative import declarative_base

#necessary for sqlalchemy to initialize the DB classes for usage.
#probably could stand to be reworked/better class organization

Base = declarative_base()
from dbManagement.dbCommandRecord import DBCommandRecord
from dbManagement.user import User
from dbManagement.dbShutdownCommand import DBShutdownCommand
from dbManagement.dbGuild import DBGuild
from dbManagement.dbGuildMember import DBGuildMember
