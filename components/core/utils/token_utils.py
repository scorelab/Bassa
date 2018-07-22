from flask import g
from Auth import verify_auth_token, generate_auth_token
from utils.app_constants import server_secret_key


def token_validator(token):
    user = verify_auth_token(token, server_secret_key)
    if user is not None:
        g.user = user
        token = generate_auth_token(user, server_secret_key)
        return token
    return None
