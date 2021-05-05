import uuid as uuid
from django.db import models
from django.db.models import Model, DateTimeField, BooleanField, CharField, ForeignKey, SET_NULL, Index
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    uuid = models.UUIDField(
        verbose_name='شناسه منحصر به فرد کاربر',
        primary_key=False,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text='unique id for users'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def check_group(self, group_name):
        if self.groups.filter(name=group_name).exists():
            return True
        else:
            return False

    def check_any_groups(self, groups_name):
        if self.groups.filter(name__in=groups_name).exists():
            return True
        else:
            return False


class BaseModel(Model):
    created_date = DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    modified_date = DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    is_active = BooleanField(default=True, verbose_name='فعال')
    related_creator = ForeignKey(
        User, on_delete=SET_NULL, blank=True, null=True, verbose_name='ایجاد کننده',
        related_name='%(class)s_creator_related',
        related_query_name='%(class)s_creator'
    )

    class Meta:
        abstract = True
        indexes = [
            Index(fields=['is_active']),
            Index(fields=['related_creator']),
            Index(fields=['is_active', 'related_creator'])
        ]
