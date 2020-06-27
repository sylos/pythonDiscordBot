
db_drivers = 'postgresql+psycopg2'
db_user = 'postgres'
db_pass = 'ThisIsMyPostgresPass#1'
db_connection_info = 'localhost/discordBotDB'

DATABASE_URI = db_drivers + '://' + db_user+':'+db_pass+'@'+db_connection_info

#DATABASE_URI = 'postgresql+psycopg2://postgres:ThisIsMyPostgresPass#1@localhost/discordBotDB'
