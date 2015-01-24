class Queue(object):

    def __init__(self, queue):
        self._queue = queue
        self.name = None

    def delete(self):
        raise NotImplementedError()


class BrokerBackend(object):

    def __init__(self):
        self._queues = None

    @property
    def queues(self):
        if self._queues is None:
            self._queues = self._get_queues()
        return self._queues

    def _get_queues(self):
        raise NotImplementedError()

    def filter_queues(self, prefix=None):
        def queue_filter(queue):
            skip = False
            if prefix:
                skip = skip or queue.name.startswith(prefix)
            return skip

        return filter(queue_filter, self.queues)
