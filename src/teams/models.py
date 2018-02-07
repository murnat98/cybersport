from api_v0_1.models import BaseAPIModel


class Teams(BaseAPIModel):
    def shard(self):
        pass

    class Meta:
        abstract = False
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
