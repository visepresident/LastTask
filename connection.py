import psycopg2

def initConnection():
  xhost = 'localhost'
  xport = 5432
  xdatabase = 'create_db'
  xuser = 'create_db'
  xpassword = 'create_db'

  connection = psycopg2.connect(
    host = xhost,
    port = xport,
    user = xuser,
    password = xpassword,
    database = xdatabase)

  connection.autocommit = True
  connection.set_client_encoding('UTF8')

  return connection

def closeConnection(pconnection):
  if pconnection is not None:
    pconnection.commit()
    pconnection.close()

  return True