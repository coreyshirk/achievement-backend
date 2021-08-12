from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def example_task(message):
    try:
        print("THIS IS A CELERY TASK")
        print('MESSAGE IN CELERY: ', message)
    except Exception as e:
        logger.error(e)
        raise self.retry(exc=e, max_retries=3)
