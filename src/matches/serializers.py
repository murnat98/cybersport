from rest_framework import serializers

from api_v0_1.serializers import default_serializer_fields
from matches.models import Matches

match_serializer_fields = default_serializer_fields + ('tournament_uuid',)


class MatchesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = match_serializer_fields


class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = match_serializer_fields
