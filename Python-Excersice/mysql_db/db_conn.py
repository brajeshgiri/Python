import mysql.connector
mydb = mysql.connector.connect(user='root', password="password", database="flask_db",
                               auth_plugin='mysql_native_password')

