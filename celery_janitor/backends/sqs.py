from celery_janitor.backends.base import BrokerBackend, Queue
from celery_janitor.exceptions import MissingDependency

try:
    from boto.sqs.connection import SQSConnection
except ImportError:
    raise MissingDependency("The 'SQS' backend requires the installation of 'boto'")


class SQSQueue(Queue):
    def __init__(self, queue):
        super(SQSQueue, self).__init__(queue)
        self._attributes = None
        self.name = self._queue.name

    @property
    def attributes(self):
        if self._attributes is None:
            self._attributes = self._get_attributes()
        return self._attributes


class SQSBackend(BrokerBackend):

    def __init__(self, aws_access_key_id, aws_secret_access_key):
        super(SQSBackend, self).__init__()
        self.connection = SQSConnection(aws_access_key_id, aws_secret_access_key)

    def _get_queues(self, prefix=None):
        return self.connection.get_all_queues(prefix)

    def delete_queue(self, queue):
        return self.connection.delete_queue(queue)
