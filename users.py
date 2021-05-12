authenticated = []


def login(username):
    if username not in authenticated:
        authenticated.append(username)
        return 1
    return -1
