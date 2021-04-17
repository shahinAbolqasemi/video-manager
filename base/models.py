from django.db.models import Model, DateTimeField, BooleanField, CharField, ForeignKey, SET_NULL, Index
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'


class BaseModel(Model):
    created_date = DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    modified_date = DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    is_active = BooleanField(default=True, verbose_name='فعال')
    creator = ForeignKey(User, on_delete=SET_NULL, blank=True, null=True, verbose_name='ایجاد کننده')

    class Meta:
        abstract = True
        indexes = [
            Index(fields=['is_active']),
            Index(fields=['creator']),
            Index(fields=['is_active', 'creator'])
        ]
