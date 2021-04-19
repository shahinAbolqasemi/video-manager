from django.db.models import CharField, Index, ForeignKey, SET_NULL, CASCADE
from base.models import BaseModel


class Service(BaseModel):
    title = CharField(max_length=128, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'
        indexes = [
            Index(fields=['title'])
        ]


class Subscription(BaseModel):
    title = CharField(max_length=128, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اشتراک'
        verbose_name_plural = 'اشتراک ها'
        indexes = [
            Index(fields=['title'])
        ]


class SubscriptionServiceAssignment(BaseModel):
    related_subscription = ForeignKey(Subscription, on_delete=SET_NULL, blank=True, null=True,
                                      verbose_name='اشتراک مربوطه')
    related_service = ForeignKey(Service, on_delete=SET_NULL, blank=True, null=True, verbose_name='سرویس مربوطه')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'سرویس در اشتراک'
        verbose_name_plural = 'سرویس های اشتراک'
        indexes = [
            Index(fields=['related_subscription']),
            Index(fields=['related_service']),
            Index(fields=['related_subscription', 'related_service'])
        ]


class ServiceField(BaseModel):
    title = CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'فیلد سرویس'
        verbose_name_plural = 'فیلدهای سرویس'
        indexes = [
            Index(fields=['title'])
        ]


class SubscriptionServiceAssignmentField(BaseModel):
    related_subscription_service_assignment = ForeignKey(SubscriptionServiceAssignment, on_delete=CASCADE)
    related_service_field = ForeignKey(ServiceField, on_delete=SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'فیلد متصل شده به سرویس اشتراک'
        verbose_name_plural = 'فیلد های متصل شده به سرویس اشتراک'
        indexes = [
            Index(fields=['related_subscription_service_assignment']),
            Index(fields=['related_service_field']),
            Index(fields=['related_subscription_service_assignment', 'related_service_field'])
        ]


class ServiceFieldAssignment(BaseModel):
    related_service = ForeignKey(to=Service, on_delete=CASCADE)
    related_service_field = ForeignKey(to=ServiceField, on_delete=CASCADE)

    class Meta:
        verbose_name = 'فیلد سرویس'
        verbose_name_plural = 'فیلد های سرویس'
        indexes = [
            Index(fields=['related_service']),
            Index(fields=['related_service_field']),
        ]
