from api_v0_1.models import BaseAPIModel


class Tournaments(BaseAPIModel):
    class Meta:
        abstract = False
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
