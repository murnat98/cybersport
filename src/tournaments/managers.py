import uuid

from api_v0_1.managers import ShardSupportManager


class TournamentsManager(ShardSupportManager):

    def create(self, **kwargs):
        if 'uuid' not in kwargs:
            kwargs['uuid'] = uuid.uuid4()

        self.sharding_scheme(uuid=uuid.uuid4())

        return super().create(**kwargs)

    @staticmethod
    def sharding_scheme(*args, **kwargs):
        """
        Sharding, according to uuid. If uuid.int is odd, than the database is the default, else it is shard_2
        """
        if 'uuid' not in kwargs:
            raise Exception

        uid = kwargs['uuid']

        if uid.int % 2:
            return 'default'
        else:
            return 'shard_2'
