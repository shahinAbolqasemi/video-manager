from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from base.views import BaseViewSet
from .models import Service, Subscription, SubscriptionServiceAssignment, ServiceField, SubscriptionServiceAssignmentField
from .serializers import ServiceSerializer, SubscriptionSerializer, SubscriptionServiceAssignmentSerializer, ServiceFieldSerializer, SubscriptionServiceAssignmentFieldSerializer


class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SubscriptionViewSet(BaseViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionServiceAssignmentViewSet(BaseViewSet):
    queryset = SubscriptionServiceAssignment.objects.all()
    serializer_class = SubscriptionServiceAssignmentSerializer


class ServiceFieldViewSet(BaseViewSet):
    queryset = ServiceField.objects.all()
    serializer_class = ServiceFieldSerializer


class SubscriptionServiceAssignmentFieldViewSet(BaseViewSet):
    queryset = SubscriptionServiceAssignmentField.objects.all()
    serializer_class = SubscriptionServiceAssignmentFieldSerializer
