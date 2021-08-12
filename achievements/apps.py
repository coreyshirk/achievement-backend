from django.apps import AppConfig


class AchievementsConfig(AppConfig):
    name = 'achievements'

    def ready(self):
        import achievements.signal_receivers # noqa
        from achievements.message_queues import ExampleQueue
        ExampleQueue().init_queue()
