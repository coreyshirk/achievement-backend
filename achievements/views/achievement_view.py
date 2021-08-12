from rest_framework import viewsets

from achievements.models import Achievement
from achievements.serializers import AchievementSerializer


class AchievementView(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'option')
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def get_queryset(self):
        return Achievement.objects.filter(
            application=self.kwargs['application_id']
        )
