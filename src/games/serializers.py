from rest_framework import serializers

from games.models import Games


class GamesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = (
            'id',
            'name',
            'description',
            'logo',
            # TODO: show url of the object
        )


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = (
            'id',
            'name',
            'description',
            'logo',
        )
