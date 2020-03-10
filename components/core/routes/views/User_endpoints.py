from flask import Blueprint
from routes.User import * 

# print(dir(user))
userprint = Blueprint("user", __name__)

userprint.add_url_rule(rule='/login',
                       endpoint='login',
                       view_func=login,
                       methods=['POST'])

userprint.add_url_rule(rule='/regularuser',
                       endpoint='regular_user_request',
                       view_func=regular_user_request,
                       methods=['POST'])

userprint.add_url_rule(rule='/user',
                       endpoint='add_user_request',
                       view_func=add_user_request,
                       methods=['POST'])

userprint.add_url_rule(rule='/user/<string:username>',
                       endpoint='remove_user_request',
                       view_func=remove_user_request,
                       methods=['DELETE'])

userprint.add_url_rule(rule='/user/<string:username>',
                       endpoint='update_user_request',
                       view_func=update_user_request,
                       methods=['PUT'])

userprint.add_url_rule(rule='/user',
                       endpoint='get_users_request',
                       view_func=get_users_request,
                       methods=['GET'])

userprint.add_url_rule(rule='/user/requests',
                       endpoint='get_user_signup_requests',
                       view_func=get_user_signup_requests,
                       methods=['GET'])

userprint.add_url_rule(rule='/user/approve/<string:username>',
                       endpoint='approve_user_request',
                       view_func=approve_user_request,
                       methods=['POST'])

userprint.add_url_rule(rule='/user/blocked',
                       endpoint='get_blocked_users_request',
                       view_func=get_blocked_users_request,
                       methods=['GET'])

userprint.add_url_rule(rule='/user/blocked/<string:username>',
                       endpoint='block_user_request',
                       view_func=block_user_request,
                       methods=['POST'])

userprint.add_url_rule(rule='/user/blocked/<string:username>',
                       endpoint='unblock_user_request',
                       view_func=unblock_user_request,
                       methods=['DELETE'])

userprint.add_url_rule(rule='/user/downloads/<int:limit>',
                       endpoint='get_downloads_user_request',
                       view_func=get_downloads_user_request,
                       methods=['GET'])

userprint.add_url_rule(rule='/user/heavy',
                       endpoint='get_topten_heaviest_users',
                       view_func=get_topten_heaviest_users,
                       methods=['GET'])
