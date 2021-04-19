from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    Participant, SessionRequest, ParticipantAssignment
)

admin.site.register(SessionRequest)
admin.site.register(Participant)
admin.site.register(ParticipantAssignment)
