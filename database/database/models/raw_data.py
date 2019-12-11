from mongoengine import ReferenceField, DictField
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
# database imports
from . import BaseDocument


class RawData(BaseDocument):
    # raw = StringField(max_length=8192, required=True)
    device = ReferenceField('Device')
    raw = DictField(required=True)
