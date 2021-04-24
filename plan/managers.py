from django.db import models
from django.utils import timezone


class ActiveSubscriptionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(expire_date__gt=timezone.now())
