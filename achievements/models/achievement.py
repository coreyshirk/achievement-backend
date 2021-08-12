from django.db import models

from achievements.models import BaseModel, Application

class Achievement(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.code
    
    class Meta:
        app_label = 'achievements'