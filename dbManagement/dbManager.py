import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy_utils import database_exists, create_database
import dbManagement.config as config


from dbManagement.base import Base

import dbManagement.user
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
    
    def test_db(self):
        message = DBCommandRecord(author='Sylos',content='The first message')
        self.session.add(message)
        self.session.commit()

    def print_hello(self, message):
        print(f'Hello {message.author.name}')

  #  def  add_message(self, message):
  #      db_message = db_convert(message)
  #      self.session.add(db_message)
  #      self.session.commit()

    #def convert_message(self, message):
     #   db_converted = DBMessage(message.author, message.content, message.created_at) 
