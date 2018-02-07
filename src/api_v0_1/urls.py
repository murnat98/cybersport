from rest_framework.routers import SimpleRouter

from games.views import GamesView
from matches.views import MatchesView
from teams.views import TeamsView
from tournaments.views import TournamentsView

app_name = 'games'

router = SimpleRouter()
router.register('games', GamesView, 'games')
router.register('tournaments', TournamentsView, 'tournaments')
router.register('matches', MatchesView, 'matches')
router.register('teams', TeamsView, 'teams')

urlpatterns = router.urls
