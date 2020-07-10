import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy_utils import database_exists, create_database
import dbManagement.config as config
import discord

from dbManagement.base import Base
from dbManagement.user import User
from dbManagement.dbShutdownCommand import DBShutdownCommand
from dbManagement.dbCommandRecord import DBCommandRecord


class DBManagement():

    def __init__(self):
        self.engine = sqlalchemy.create_engine(config.DATABASE_URI)

        #need to test if I can connect to the DB at all. Useful when DB is no longer on box

        print("Testing if DB exists")
        if not database_exists(self.engine.url):
            print("Creating DB since it does not exist")
            create_database(self.engine.url)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        Base.metadata.create_all(self.engine)
        self.session.commit()
    
    def print_hello(self, message):
        print(f'Hello {message.author.name}')

    def test_db(self):
        message = DBCommandRecord(author='Sylos',content='The first message')
        self.session.add(message)
        self.session.commit()

    def add_db_command_record(self, message):
        db_message = self.convert_to_record(message)
        self.session.add(db_message)
        self.session.commit()
 
    def add_guild(self, guild):
        #addGuildToDB

        members = self.get_guild_members(guild)
        self.add_guild_users(members)
      
    def get_guild_members(self, guild):
        members = []
        for x in guild.members:
            members.append(x.id)

        return members

    def add_shutdown_command(self, message, restart=True):
        shutdown_record = DBShutdownCommand(
            author_id = message.author.id,
            shutdown_at = message.created_at,
            channel_id = message.channel.id,
            restart = restart)

        self.add_item(shutdown_record)
        return

    def query_latest_shutdown(self):
        latest_shutdown = self.session.query(
                DBShutdownCommand).order_by(
                        DBShutdownCommand.shutdown_at.desc()).first()

        return latest_shutdown
    #potential slowpoint
    def add_user(self, member):
        self.session.add(User(unique_user_id = member))
        self.session.commit()

    def add_guild_users(self, members):
        new_users = []
        new_user_ids = []
        filtered_users = []
        filtered_ids = []
        print(f"Members: {members}")
        for member in members:
            new_user_ids.append(member)

        filtered_users = self.session.query(User).with_entities(User.unique_user_id).filter(User.unique_user_id.in_(new_user_ids)).all()

        for x in filtered_users:
            filtered_ids.append(x.unique_user_id)

        new_users = set(new_user_ids).difference(filtered_ids) 
         
        for u_u_id in new_users:
            self.session.add(User(unique_user_id=u_u_id))

        self.session.commit()


    def add_item(self, item):
        self.session.add(item)
        self.session.commit()

    def convert_to_record(self, message):
        dmChannel = isinstance(message.channel, discord.DMChannel)
        db_converted = DBCommandRecord(author=message.author.name
                , content=message.content
                , channel=message.channel.recipient.name if dmChannel else message.channel.name
                , guild=None if dmChannel else message.guild.name
                , message_id=message.id
                , message_created_at=message.created_at) 
        return db_converted

