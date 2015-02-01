import unittest

import mock

from celery_janitor.utils import Config


class ConfigTest(unittest.TestCase):

    @mock.patch('celery_janitor.utils.conf.BROKER_URL', 'sqs://aws_access_key_id:aws_secret@')
    def test_sqs_backend(self):
        self.config = Config()
        backend = self.config.get_backend_class()
        self.assertEqual(backend, 'celery_janitor.backends.sqs.SQSBackend')
        key, secret = self.config.get_credentials()
        self.assertEqual(key, 'aws_access_key_id')
        self.assertEqual(secret, 'aws_secret')
