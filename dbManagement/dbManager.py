import psycopg2
import sqlalchemy
import sqlalchemy_utils


Base = declarative_base()

db_connection_info = 'localhost/discordBotDB'
db_user = 'postgres'
db_pass = 'ThisIsMyPostgresPass#1'




class DBManagement():

    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://'
                +db_user+':'+db_pass+'@'+db_connection_info)

        #need to test if I can connect to the DB at all. Useful when DB is no longer on box

        print("Testing if DB exists")
        if not database_exists(self.engine.url):
            print("Creating DB since it does not exist")
            create_database(self.engine.url)

        self.Session = sessionMaker(bind=self.engine)
        self.session - self.Session()

        
