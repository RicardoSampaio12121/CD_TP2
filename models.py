from flask_login import UserMixin


class UserModel:

    def __init__(self, username, password):
        self._username = username
        self._password = password


