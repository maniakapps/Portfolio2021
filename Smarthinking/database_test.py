import mysql.connector

__CONFIG_FILE = 'mysql_credentials.txt'
_user: str = ''
_password: str = ''
_host = ''
_database: str = ''

with open(__CONFIG_FILE) as file:
    __config = file.readline().split(',')
    _user = __config[0]
    _password = __config[1]
    _host = __config[2]
    _database = __config[3]

try:
    conn = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
    print("Succesful connection")
    conn.close()
except mysql.connector.errors as e:
    print(e)
