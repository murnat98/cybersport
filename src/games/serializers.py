from rest_framework import serializers

from api_v0_1.serializers import default_serializer_fields
from games.models import Games


class GamesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = default_serializer_fields


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = default_serializer_fields
