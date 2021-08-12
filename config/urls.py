from django.urls import path, include
from django.conf.urls import url, re_path
from achievements.views.healthcheck_view import healthcheck

urlpatterns = [
    re_path(r'^api/', include('achievements.urls')),
    re_path(r'^healthchecks', healthcheck),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
