import mysql.connector


class UserManagement:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_user(self):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='2862',
                                       database='cdtp2')

        mycursor = mydb.cursor()

        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (self.username, self.password)
        mycursor.execute(sql, val)

        mydb.commit()




