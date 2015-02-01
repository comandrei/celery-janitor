import urlparse

from celery_janitor import conf
from celery_janitor.exceptions import BackendNotSupportedException


BACKEND_MAPPING = {
    'sqs': 'celery_janitor.backends.sqs.SQSBackend'
}


class Config(object):

    def __init__(self):
        self.broker = urlparse.urlparse(conf.BROKER_URL)

    def get_backend(self):
        try:
            return BACKEND_MAPPING[self.broker.scheme]
        except KeyError:
            raise BackendNotSupportedException(
                "{} not supported".format(self.broker.scheme))

    def get_credentials(self):
        if self.broker.scheme == 'sqs':
            access_id, access_secret = self.broker.netloc.split(':')
            access_secret = access_secret[:-1]
            return (access_id, access_secret)
