import datetime
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

from mongoengine import Document, DateTimeField


class BaseDocument(Document):
    meta = {
        'abstract': True,
    }
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

    def clean(self):
        # https://stackoverflow.com/questions/6102103/using-mongoengine-document-class-methods-for-custom-validation-and-pre-save-hook
        # if self.status == 'Draft' and self.pub_date is not None:
        #     raise ValidationError('Draft entries should not have a publication date.')

        # Set the pub_date for published items if not set.
        now = datetime.datetime.utcnow()
        if self.date_modified < now:
            self.date_modified = now
