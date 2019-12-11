from mongoengine import StringField
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
# database imports
from . import BaseDocument


class Authorization(BaseDocument):
    name = StringField(required=True)
