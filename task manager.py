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

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your MySQL username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: The specified database does not exist.")
    else:
        print(f"Error: {err}")
    exit()
