from rest_framework.routers import SimpleRouter

from games.views import GamesView

app_name = 'games'

router = SimpleRouter()
router.register('games', GamesView, 'games')

urlpatterns = router.urls
