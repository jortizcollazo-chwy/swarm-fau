from mongoengine import StringField, DictField
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
# database imports
from . import BaseDocument


class Project(BaseDocument):
    name = StringField(required=True, unique=True)
    description = StringField()
    img = StringField()
    link = StringField()
