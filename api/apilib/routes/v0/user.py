from __future__ import print_function, absolute_import
import os
import sys
import logging
import requests
import bson
from flask import (Blueprint, abort, request, jsonify, Response, session, current_app)

# database lib imports
from database.models.user import User

# app imports
from apilib.lib import add_headers
from apilib.lib.exceptions import AugmentedException

FILE_DIR = os.path.dirname(__file__)
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

user_route = Blueprint('user_route', __name__)


@user_route.route('user', methods=['POST', 'GET', 'OPTIONS'])
@user_route.route('user/<user_id>', methods=['GET', 'PUT', 'DELETE', 'OPTIONS'])
def user(*args, **kwargs):
    args = current_app.config['args']
    headers = current_app.config['headers']

    response = Response()
    route_params = request.view_args
    get_params = request.args.to_dict(flat=False)
    if request.method in ['POST', 'PUT', 'DELETE']:
        body = request.json

    message = []
    data = None
    error = None
    try:
        if request.method == 'POST':
            data = User(**body)
            data.save()
            data = data.to_mongo()
        elif request.method == 'GET':
            data = [obj.to_mongo() for obj in User.objects]
        elif request.method == 'PUT':
            _id = route_params['user_id']
            data = User.objects(id=bson.ObjectId(_id))
            for attr in ['first_name', 'last_name', 'email', 'password', 'authorization']:
                if body.get(attr) is not None:
                    setattr(data, attr, body[attr])
            data.save()
            data = data.to_mongo()
        elif request.method == 'DELETE':
            _id = route_params['user_id']
            data = User.objects(id=bson.ObjectId(_id))
            data.delete()
        elif request.method == 'OPTIONS':
            pass
        else:
            pass

    except Exception as e:
        error = AugmentedException(e).to_dict()
        LOGGER.error('', exc_info=True)

    response = jsonify(message=message, data=data, error=error)
    response = add_headers(response, headers=headers)
    LOGGER.warning(vars(response))
    return response