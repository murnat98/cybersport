from rest_framework.routers import SimpleRouter

from games.views import GamesView
from matches.views import MatchesView
from tournaments.views import TournamentsView

app_name = 'games'

router = SimpleRouter()
router.register('games', GamesView, 'games')
router.register('tournaments', TournamentsView, 'tournaments')
router.register('matches', MatchesView, 'matches')

urlpatterns = router.urls
