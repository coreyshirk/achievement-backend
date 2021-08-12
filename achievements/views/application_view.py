from rest_framework import viewsets

from achievements.models import Application
from achievements.serializers import ApplicationSerializer


class ApplicationView(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'option')
    queryset = Application.objects.all().order_by('id')
    serializer_class = ApplicationSerializer
