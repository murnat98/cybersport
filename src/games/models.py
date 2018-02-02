from api_v0_1.models import BaseAPIModel


class Games(BaseAPIModel):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['name', ]
