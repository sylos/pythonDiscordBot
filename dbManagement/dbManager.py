import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy_utils import database_exists, create_database
import dbManagement.config as config


from dbManagement.base import Base

import dbManagement.user
from dbManagement.dbMessage import DBMessage


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
        message = DBMessage(author='Sylos',content='The first message')
        self.session.add(message)
        self.session.commit()

#    def  add_message(self, message: Message):
#        self.session.add(message)
#        self.session.commit()

    
