from datetime import datetime

from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    port = models.IntegerField(null=False)
    last_presence = models.DateTimeField(default=datetime.now)
