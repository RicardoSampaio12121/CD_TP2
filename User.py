import mysql.connector


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='2862',
                                          database='cdtp2')

    @property
    def get_username(self):
        return self.username

    @property
    def get_password(self):
        return self.password

    def create_user(self):
        my_cursor = self.db.cursor()

        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (self.username, self.password)
        my_cursor.execute(sql, val)
        self.db.commit()

    def authenticate_user(self):
        my_cursor = self.db.cursor()

        my_cursor.execute("SELECT *FROM user WHERE username ='%s' AND password ='%s'" % (self.username, self.password))

        account = my_cursor.fetchone()

        if account:
            return True
        return False

    def messenger_load_people(self, username):
        my_cursor = self.db.cursor()

        mycursor.execute("SELECT")
