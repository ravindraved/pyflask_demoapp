user = [

    {
        'id': 1,
        'username': 'ravi',
        'password': 'ravi1'
    },
    {
        'id': 2,
        'username': 'aditya',
        'password': 'aditya1'

    }

]

user_mapping = {

    'ravi': {
        'id': 1,
        'username': 'ravi',
        'password': 'ravi1'

    },

    'aditya': {

        'id': 2,
        'username': 'aditya',
        'password': 'aditya1'

    }

}

userid_mapping = {

    1: {
        'id': 1,
        'username': 'ravi',
        'password': 'ravi1'

    },

    2: {
        'id': 2,
        'username': 'aditya',
        'password': 'aditya1'

    }
}


def authenticate(username,password):
    user = user_mapping.get(username, None)
    if user and user.get('password') == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)


print("authentication->", authenticate('ravi','ravi'))