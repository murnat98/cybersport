from api_v0_1.models import BaseAPIModel


class Games(BaseAPIModel):
    class Meta:
        abstract = False
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
