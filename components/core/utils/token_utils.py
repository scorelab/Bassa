from flask import g
from Auth import verify_auth_token, generate_auth_token
from utils.app_constants import SERVER_SECRET_KEY



def token_validator(token):
    user = verify_auth_token(token, SERVER_SECRET_KEY)
    if user is not None:
        g.user = user
        token = generate_auth_token(user, SERVER_SECRET_KEY)
        return token
    return None
