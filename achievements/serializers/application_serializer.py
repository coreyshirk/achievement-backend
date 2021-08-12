from rest_framework import serializers

from achievements.models import Application
from achievements.signals import example_food_print

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'

    def save(self, **kwargs):
        instance = super(ApplicationSerializer, self).save(**kwargs)
        print('PRE-SIGNAL')
        example_food_print.send(
            sender=self.__class__, message="Save method in FoodSerializer"
        )
        print("POST-SIGNAL")
        return instance