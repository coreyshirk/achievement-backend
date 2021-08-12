from django.db import models

from achievements.models import BaseModel

class Application(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'achievements'