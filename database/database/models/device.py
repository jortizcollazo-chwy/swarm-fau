import datetime
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

from mongoengine import StringField, DictField


from . import BaseDocument


class Device(BaseDocument):
    name = StringField(max_length=128, required=True)
    meta_data = DictField()
