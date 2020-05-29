from dobj.user_do import UserDo
from werkzeug.security import safe_str_cmp

# safe string compare to account for unicode characters.. mostly for python versions 2

userslist = [
    UserDo(1, "ravi", "ravi1"),
    UserDo(2, "aditya", "aditya1")
]

username_mapping = {u.username: u for u in userslist}
userid_mapping = {u.id: u for u in userslist}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)


print(authenticate('ravi','rav1'))
