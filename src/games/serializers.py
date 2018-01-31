from rest_framework import serializers

from games.models import Games


class GamesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = (
            'name',
            'description',
            'logo',
        )
