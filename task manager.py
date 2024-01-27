import mysql.connector #pip install mysql-connector-python
from mysql.connector import errorcode


# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host='sql_host',
        user='mysql_user',
        password='mysql_password',
        database='task_manager'
    )