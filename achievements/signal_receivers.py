from django.dispatch import receiver

from .tasks import example_task
from .signals import example_food_print

@receiver(example_food_print, dispatch_uid='example_food_print')
def example_food_print(sender, message, **kwargs):
    print('FOOBAR RECEIVER')
    example_task.delay(message)
    print('THIS IS THE example_food_print with message: ', message)