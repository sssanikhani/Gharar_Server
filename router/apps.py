from django.apps import AppConfig

import threading

from router.tasks import remove_non_present_members


class RouterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'router'

    def ready(self):
        th = threading.Thread(target=remove_non_present_members)
        th.start()
