from api_v0_1.models import BaseAPIModel
from tournaments.managers import TournamentsManager


class Tournaments(BaseAPIModel):
    manager = TournamentsManager
    objects = manager()

    class Meta:
        abstract = False
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
