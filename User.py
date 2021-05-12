import mysql.connector


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def get_username(self):
        return self.username

    @property
    def get_password(self):
        return self.password

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

    def authenticate_user(self):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='2862',
                                       database='cdtp2')

        mycursor = mydb.cursor()

        mycursor.execute("SELECT *FROM user WHERE username ='%s' AND password ='%s'" % (self.username, self.password))

        account = mycursor.fetchone()

        if account:
            return True
        return False
