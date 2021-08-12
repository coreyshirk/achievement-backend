from rest_framework import routers

from achievements.views import (
    ApplicationView,
    AchievementView,
)

router = routers.SimpleRouter()
router.register(r'applications', ApplicationView)
router.register(r'applications/(?P<application_id>\d+)/achievement', AchievementView)

urlpatterns = router.urls
