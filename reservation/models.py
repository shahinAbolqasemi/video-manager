from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from plan.models import Service, ServiceField


class ServiceRequest(BaseModel):
    groups_count = models.PositiveIntegerField(verbose_name=_('group count'))
    unique_id = models.CharField(verbose_name=_('unique id'), max_length=5, unique=True)
    related_customer = models.ForeignKey(
        verbose_name=_('customer'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='%(class)s_customer_related',
        related_query_name='%(class)s_customer'
    )
    is_accepted = models.BooleanField(verbose_name=_('is accepted'), default=False)
    start_date = models.DateTimeField(verbose_name=_('start date'))
    end_date = models.DateTimeField(verbose_name=_('end date'))
    related_participants = models.ManyToManyField(
        verbose_name=_('participants'),
        to='Participant',
        through='ParticipantAssignment',
        through_fields=('related_session_request', 'related_participant'),
        related_name='%(class)s_participants_related',
        related_query_name='%(class)s_participants'
    )


class SessionRequestServiceFieldAssignment(BaseModel):
    related_service = models.ForeignKey(
        verbose_name=_('service'),
        to=Service,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(class)s_service_related',
        related_query_name='%(class)s_service'
    )
    related_service_request = models.ForeignKey(
        verbose_name=_('service request'),
        to=ServiceRequest,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(class)s_service_request_related',
        related_query_name='%(class)s_service_request'
    )
    related_service_field = models.ForeignKey(
        verbose_name=_('service field'),
        to=ServiceField,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(class)s_service_field_related',
        related_query_name='%(class)s_service_field'
    )
    amount = models.IntegerField(verbose_name=_('amount'), default=0)


class Participant(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=200, unique=True)

    class Meta:
        verbose_name = _('participant')
        verbose_name_plural = _('participants')


class ParticipantAssignment(BaseModel):
    related_session_request = models.ForeignKey(
        verbose_name=_('service request'),
        to='ServiceRequest',
        on_delete=models.PROTECT,
        related_name='%(class)s_service_request_related',
        related_query_name='%(class)s_service_request'
    )
    related_participant = models.ForeignKey(
        verbose_name=_('participant request'),
        to='Participant',
        on_delete=models.PROTECT,
        related_name='%(class)s_participant_related',
        related_query_name='%(class)s_participant'
    )

    class Meta:
        verbose_name = _('participant assignment')
        verbose_name_plural = _('participant assignments')
        constraints = [
            models.UniqueConstraint(
                fields=('related_session_request', 'related_participant'),
                name='unique_session_participant'
            ),
        ]
