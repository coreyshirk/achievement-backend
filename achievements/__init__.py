from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

default_app_config = 'achievements.apps.AchievementsConfig'

__all__ = ('celery_app', )
