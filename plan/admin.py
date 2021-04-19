from django.contrib.admin import ModelAdmin, site
from .models import Service, Subscription, SubscriptionServiceAssignment, ServiceField, \
    SubscriptionServiceAssignmentField, ServiceFieldAssignment


class ServiceAdmin(ModelAdmin):
    list_display = ['pk', 'title']


class SubscriptionAdmin(ModelAdmin):
    list_display = ['pk', 'title']


class SubscriptionServiceAssignmentAdmin(ModelAdmin):
    list_display = ['pk', 'related_subscription', 'related_service']


class ServiceFieldAdmin(ModelAdmin):
    list_display = ['pk', 'title']


class SubscriptionServiceAssignmentFieldAdmin(ModelAdmin):
    list_display = ['pk', 'related_subscription_service_assignment', 'related_service_field']


class ServiceFieldAssignmentAdmin(ModelAdmin):
    list_display = ['pk', 'related_service', 'related_service_field']


site.register(Service, ServiceAdmin)
site.register(Subscription, SubscriptionAdmin)
site.register(SubscriptionServiceAssignment, SubscriptionServiceAssignmentAdmin)
site.register(ServiceField, ServiceFieldAdmin)
site.register(SubscriptionServiceAssignmentField, SubscriptionServiceAssignmentFieldAdmin)
site.register(ServiceFieldAssignment, ServiceFieldAssignmentAdmin)
