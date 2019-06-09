from db_conn import mydb


# mydb = mysql.connector.connect(user='root', password="password", database="flask_db",
#                                auth_plugin='mysql_native_password')


def insertRecord():
    try:
        mycursor = mydb.cursor()
        j = 0
        while j < 10:
            i = "test"
            sql = "INSERT INTO tbl_user (user_name, user_email,user_password) VALUES (%s, %s, %s)"
            val = ("user name " + i, "user_@gmail.com", "pass" + i)
            mycursor.execute(sql, val)
            j = j + 1

        mydb.commit()
        # mydb.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def deleteAll():
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM tbl_user");
    mydb.commit();
    # mydb.close();


def selectAll():
    print(mydb)
    mycursor = mydb.cursor();
    mycursor.execute("SELECT * FROM tbl_user")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


insertRecord()
selectAll()

deleteAll()
