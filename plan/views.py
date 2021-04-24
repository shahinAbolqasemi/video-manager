from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from base.views import BaseViewSet
from .models import Service, Subscription, SubscriptionServiceAssignment, ServiceField, \
    SubscriptionServiceAssignmentField, ServiceFieldAssignment, SubscriptionAssignment
from .serializers import ServiceSerializer, SubscriptionSerializer, SubscriptionServiceAssignmentSerializer, \
    ServiceFieldSerializer, SubscriptionServiceAssignmentFieldSerializer, ServiceFieldAssignmentSerializer, \
    SubscriptionAssignmentSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


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


class ServiceFieldAssignmentViewSet(BaseViewSet):
    queryset = ServiceFieldAssignment.objects.all()
    serializer_class = ServiceFieldAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_service']


class SubscriptionAssignmentViewSet(BaseViewSet):
    queryset = SubscriptionAssignment.objects.all()
    serializer_class = SubscriptionAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

