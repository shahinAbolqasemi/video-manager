from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    Participant, ServiceRequest, ParticipantAssignment
)

admin.site.register(ServiceRequest)
admin.site.register(Participant)
admin.site.register(ParticipantAssignment)
