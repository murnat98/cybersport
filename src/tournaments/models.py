from api_v0_1.models import BaseAPIModel


class Tournaments(BaseAPIModel):
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        uuid = self.uuid
        if uuid.int % 2:
            using = 'default'
        else:
            using = 'shard_2'

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = False
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
