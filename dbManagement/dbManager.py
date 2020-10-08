
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy_utils import database_exists, create_database
import dbManagement.config as config
import discord

from dbManagement.base import Base
from dbManagement.user import User
from dbManagement.dbShutdownCommand import DBShutdownCommand
from dbManagement.dbCommandRecord import DBCommandRecord
from dbManagement.dbGuild import DBGuild
from dbManagement.dbGuildMember import DBGuildMember

#A manager for the database.  It handles connections
#to the DB, queries to and from the DB, etc.
#I'm not sure how necessary it is, but I think it's
#the seed of good design

class DBManagement():

    #Init for the manager
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

    #shutdown query, cleans up the DB
    def shutdown(self):
        self.session.close()
        self.engine.dispose()

    #a test command to the DB if it's working.  Could be removed with 
    #testing improvements.
    def test_db(self):
        message = DBCommandRecord(author='Sylos',content='The first message')
        self.session.add(message)
        self.session.commit()

    #This adds a master record of every command the bot runs, to the DB
    def add_db_command_record(self, message):
        db_message = self.convert_to_record(message)
        self.session.add(db_message)
        self.session.commit()
 
    #adds a specific shutdown command.  Tracks
    #author who sent it, the time, the channel the message came in
    #and whether it's a shutdown or restart
    def add_shutdown_command(self, message, restart=True):
        shutdown_record = DBShutdownCommand(
            author_id = message.author.id,
            shutdown_at = message.created_at,
            channel_id = message.channel.id,
            restart = restart)

        self.add_item(shutdown_record)
        return

    #gets the last shutdown command and returns it.  Used for 
    #sending the awoken message a specific channel
    def query_latest_shutdown(self):
        latest_shutdown = self.session.query(
                DBShutdownCommand).order_by(
                        DBShutdownCommand.shutdown_at.desc()).first()

        return latest_shutdown

    #runs a query that grabs the all the users from a discord server
    #and a)sees if we already have a record of the user and b)
    #adds the user to the channel
    #slowpoint singly adding users. Will fix up later
    def join_guild(self, guild):
        if self.get_guild(guild) is None:
            guild_record = self.add_guild(guild)
            for member in guild.members:
                user = self.add_user(member)
                guild_member = self.add_guild_member(member.id, guild.id)
                guild_member.user = user
                guild_member.guild = guild_record
                guild_record.members.append(guild_member)
                self.session.add(user)
            
                self.session.add(guild_member)

            self.session.add(guild_record)
            self.session.commit()
            


    #returns whether a guild is in the databse or not
    def get_guild(self, guild):
        filter_guild = self.session.query(DBGuild).filter(DBGuild.guild_id == guild.id).first()
        return filter_guild

    #adds a guild to the database
    def add_guild(self, guild):
        return DBGuild(guild_id=guild.id)

    #adds guild members to the database.  
    def add_guild_member(self, member_id, guild_id):
        filtered_membership = self.session.query(DBGuildMember).filter(
                DBGuildMember.user_id==member_id 
                , DBGuildMember.guild_id==guild_id).first()
        if filtered_membership is None:
            return DBGuildMember(present=True)

        return filtered_membership
  
    #gets the list of guilds members from the server
    def get_guild_members(self, guild):
        members = []
        for x in guild.members:
            members.append(x.id)

        return members

    #adds an individual user to the database.
    #checks to see if the user in the database already

    def add_user(self, member):
        filtered_user = self.session.query(User).filter(User.unique_user_id == member.id).first()
        if filtered_user is None:
            return User(unique_user_id=member.id)
        return filtered_user

    #A modified version of guild users.  I have multiple copies of similar
    #methods.  I was testing slightly different ways of approaching 
    #adding guild users.  While not usually relevant, sometimes
    #the guild lists can be quite large(thousands)
    def add_guild_users(self, members, guild, guild_record):
        new_users = []
        new_user_ids = []
        filtered_users = []
        filtered_ids = []

        #We get the ids because sqlalchemy wasn't returning just the id column when trying, or a proper record.  Need to rewrite later
        for member in members:
            new_user_ids.append(member)

        #get the list of users already inside the user table.  This is 'old' users
        filtered_users = self.session.query(User).filter(User.unique_user_id.in_(new_user_ids)).all()

        #get their IDs.  Need to rewrite again.  It's dumb and it was late
        #added in the append onto the new guild.  Need to rewrite
        for x in filtered_users:
            filtered_ids.append(x.unique_user_id)
            x.guilds.append(guild_record)
            self.session.add(x)


        #get new, unique users that are not already inside the table.
        new_users = set(new_user_ids).difference(filtered_ids) 
         
        #add new users to DB
        for u_u_id in new_users:
            self.session.add(User(unique_user_id=u_u_id, guilds=[guild_record]))

        self.session.commit()

        for member in guild.members:
            if member.id in filtered_ids:
                member.guilds.append(guild_record)

    #adds a generic item to the database.  I added this for generic reasons
    #I intend rewrite various objects to make use of item functionality
    def add_item(self, item):
        self.session.add(item)
        self.session.commit()

    #cleans up a discord API/discord.py message object and 
    #discards unused information and prepares it to store it in
    #the DB
    def convert_to_record(self, message):
        dmChannel = isinstance(message.channel, discord.DMChannel)
        db_converted = DBCommandRecord(author=message.author.name
                , content=message.content
                , channel=message.channel.recipient.name if dmChannel else message.channel.name
                , guild=None if dmChannel else message.guild.name
                , message_id=message.id
                , message_created_at=message.created_at) 
        return db_converted

