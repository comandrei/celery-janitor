import importlib
import urlparse

from celery_janitor import conf
from celery_janitor.exceptions import BackendNotSupportedException


BACKEND_MAPPING = {
    'sqs': 'celery_janitor.backends.sqs.SQSBackend'
}


def import_class(path):
    path_bits = path.split('.')
    class_name = path_bits.pop()
    module_path = '.'.join(path_bits)
    module_itself = importlib.import_module(module_path)

    if not hasattr(module_itself, class_name):
        raise ImportError("Module '%s' has no '%s' class." % (module_path, class_name))

    return getattr(module_itself, class_name)


class Config(object):

    def __init__(self):
        self.broker = urlparse.urlparse(conf.BROKER_URL)

    def get_backend_class(self):
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


def get_backend():
    config = Config()
    backend_class = config.get_backend()
    backend = import_class(backend_class)
    return backend(*config.get_credentials())
