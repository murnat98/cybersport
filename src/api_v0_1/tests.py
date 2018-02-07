from django.db import models
from django.test import TestCase


class BaseShardingTest(TestCase):
    model = None
    iter = ()

    creation_kwargs = {}

    def setUp(self):
        """
        Create test objects in databases
        """
        self.setup_objects = []
        for iter_obj in self.iter:
            assert issubclass(self.model, models.Model)

            self.creation_kwargs = self._get_creation_kwargs(iter_obj)
            self.setup_objects.append(self.model.objects.create(**self.creation_kwargs))

    def _get_creation_kwargs(self, iter_obj):
        """
        Count creation kwargs on each name.
        :param iter_obj: the name of object
        :return: creation kwargs dict
        :rtype: dict
        """
        raise NotImplementedError('`_get_creation_kwargs` not implemented')

    def _in_right_shard(self, obj, *args, **kwargs):
        """
        :return: True if obj is in right shard database, else returns False
        :rtype: bool
        """
        raise NotImplementedError('`_in_right_shard` not implemented')

    def tearDown(self):
        for obj in self.setup_objects:
            obj.delete()
