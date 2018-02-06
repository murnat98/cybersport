from django.core.exceptions import ObjectDoesNotExist


class TournamentNotFoundError(ObjectDoesNotExist):
    """Tournament object not found in all databases."""
