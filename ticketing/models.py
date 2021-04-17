from django.db.models import CharField, Index, ForeignKey, SET_NULL, CASCADE, FileField, TextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import BaseModel, User
from plan.models import Subscription


class TicketCategory(BaseModel):
    title = CharField(max_length=128, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی تیکت'
        verbose_name_plural = 'دسته بندی های تیکت'
        indexes = [
            Index(fields=['title'])
        ]

class Priority(BaseModel):
    title = CharField(max_length=32, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اولویت'
        verbose_name_plural = 'اولویت ها'
        indexes = [
            Index(fields=['title'])
        ]


class TicketStatus(BaseModel):
    title = CharField(max_length=32, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'وضعیت تیکت'
        verbose_name_plural = 'وضعیت های تیکت'
        indexes = [
            Index(fields=['title'])
        ]


class Ticket(BaseModel):
    subject = CharField(max_length=32, verbose_name='موضوع')
    related_priority = ForeignKey(Priority, on_delete=SET_NULL, blank=True, null=True, verbose_name='اولویت')
    related_ticket_category = ForeignKey(TicketCategory, on_delete=SET_NULL, blank=True, null=True, verbose_name='بخش مربوطه')
    related_subscription = ForeignKey(Subscription, on_delete=SET_NULL, blank=True, null=True, verbose_name='اشتراک مربوطه')
    related_ticket_status = ForeignKey(TicketStatus, on_delete=SET_NULL, blank=True, null=True, verbose_name='وضعیت تیکت مربوطه')
    email = CharField(max_length=128, verbose_name='آدرس ایمیل')
    referred_to_ticket_category = ForeignKey(TicketCategory, on_delete=SET_NULL, blank=True, null=True, related_name='ticket_referred_to_ticket_category', verbose_name='ارجاع شده به بخش تیکتینگ')
    referred_to_user = ForeignKey(User, on_delete=SET_NULL, blank=True, null=True, related_name='ticket_referred_to_user', verbose_name='ارجاع شده به کاربر')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'
        indexes = [
            Index(fields=['related_priority']),
            Index(fields=['related_ticket_category']),
            Index(fields=['related_subscription']),
            Index(fields=['email']),
            Index(fields=['referred_to_ticket_category']),
            Index(fields=['referred_to_user']),
            Index(fields=['related_priority', 'related_ticket_category']),
            Index(fields=['related_priority', 'related_subscription']),
            Index(fields=['related_ticket_category', 'related_subscription']),
            Index(fields=['related_priority', 'related_ticket_category', 'related_subscription'])
        ]


class TicketMessage(BaseModel):
    related_ticket = ForeignKey(Ticket, on_delete=CASCADE, verbose_name='تیکت مربوطه')
    text = TextField(blank=True, null=True, verbose_name='متن')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'پیام تیکت'
        verbose_name_plural = 'پیام های تیکت'
        indexes = [
            Index(fields=['related_ticket'])
        ]


class TicketFileAttachment(BaseModel):
    related_ticket_message = ForeignKey(TicketMessage, on_delete=CASCADE, verbose_name='پیام مربوطه')
    file = FileField(verbose_name='فایل پیوست')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'فایل پیوست تیکت'
        verbose_name_plural = 'فایل های پیوست تیکت'
        indexes = [
            Index(fields=['related_ticket_message'])
        ]


class TicketComment(BaseModel):
    related_ticket = ForeignKey(Ticket, on_delete=CASCADE, verbose_name='تیکت مربوطه')
    text = TextField(verbose_name='متن')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'کامنت تیکت'
        verbose_name_plural = 'کامنت های تیکت'
        indexes = [
            Index(fields=['related_ticket'])
        ]


class TicketCategoryUserAssignment(BaseModel):
    related_ticket_category = ForeignKey(TicketCategory, on_delete=CASCADE, verbose_name='دسته بندی تیکت مربوطه')
    related_user = ForeignKey(User, on_delete=CASCADE, related_name='ticket_category_user_assignment_related_user', verbose_name='کاربر مربوطه')

    def __str__(self):
        return self.related_user.username

    class Meta:
        verbose_name = 'کارشناس مدیریت تیکت'
        verbose_name_plural = 'کارشناس های مدیریت تیکت'
        indexes = [
            Index(fields=['related_ticket_category']),
            Index(fields=['related_user']),
            Index(fields=['related_ticket_category', 'related_user'])
        ]


class TicketCategoryReferRequest(BaseModel):
    related_ticket = ForeignKey(Ticket, on_delete=CASCADE, verbose_name='تیکت مربوطه')
    related_ticket_category = ForeignKey(TicketCategory, on_delete=SET_NULL, blank=True, null=True, verbose_name='دسته بندی مربوطه')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'درخواست ارجاع به بخش تیکتینگ'
        verbose_name_plural = 'درخواست های ارجاع به بخش تیکتینگ'
        indexes = [
            Index(fields=['related_ticket']),
            Index(fields=['related_ticket_category']),
            Index(fields=['related_ticket', 'related_ticket_category'])
        ]


@receiver(post_save, sender=TicketCategoryReferRequest, dispatch_uid="update_ticket_refer_field")
def update_ticket(sender, instance, **kwargs):
    ticket = instance.related_ticket
    ticket.referred_to_ticket_category = instance.related_ticket_category
    ticket.referred_to_user = None
    ticket.save()


class UserReferRequest(BaseModel):
    related_ticket = ForeignKey(Ticket, on_delete=CASCADE, verbose_name='تیکت مربوطه')
    related_user = ForeignKey(User, on_delete=CASCADE, related_name='user_refer_request_related_user', verbose_name='کاربر مربوطه')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'درخواست ارجاع به کاربر'
        verbose_name_plural = 'درخواست های ارجاع به کاربر'
        indexes = [
            Index(fields=['related_ticket']),
            Index(fields=['related_user']),
            Index(fields=['related_ticket', 'related_user'])
        ]

def user_refer_update_ticket(sender, instance, **kwargs):
    ticket = instance.related_ticket
    ticket.referred_to_user = instance.related_user
    ticket.referred_to_ticket_category = None
    ticket.save()
