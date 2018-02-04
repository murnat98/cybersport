from django.db import models

from api_v0_1.exceptions import NotSupportedFunction


class ShardSupportManager(models.Manager):
    """
    Manager supporting database sharding
    """

    def __init__(self):
        self._db = None
        super().__init__()

    def create(self, **kwargs):
        """
        Creating objects, according to sharding scheme.
        TODO: write more global function
        """
        return super().create(**kwargs)

    def bulk_create(self, objs, batch_size=None):
        """
        Bulk creating not supported with sharding.
        """
        raise NotSupportedFunction('`bulk_create` function not supported for sharding databases!')

    @staticmethod
    def sharding_scheme(*args, **kwargs):
        """
        :param: kwargs - the fields dictionary, passed from create function
        :return: database name, according to sharding scheme
        """
        raise NotImplementedError('`sharding_scheme` function not implemented!')
