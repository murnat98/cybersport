from django.contrib import admin

from games.models import Games


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    pass
