from django.db import models

from achievements.models import BaseModel

class Task(BaseModel):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    operand = models.ForeignKey(Operand, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'achievements'