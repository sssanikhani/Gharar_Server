import datetime
import time


def remove_non_present_members():
    while True:
        time.sleep(5)
        from .models import Member
        not_present = Member.objects.filter(last_presence__lt=datetime.datetime.now() - datetime.timedelta(seconds=5))
        not_present.delete()