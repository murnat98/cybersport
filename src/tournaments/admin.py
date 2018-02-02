from django.contrib import admin

from tournaments.models import Tournaments


@admin.register(Tournaments)
class TournamentsAdmin(admin.ModelAdmin):
    pass
