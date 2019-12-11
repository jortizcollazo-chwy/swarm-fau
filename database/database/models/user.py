from mongoengine import StringField, DictField
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
# database imports
from . import BaseDocument


class User(BaseDocument):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    authorization = DictField()