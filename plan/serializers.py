from rest_framework.serializers import ModelSerializer
from .models import Service, Subscription, SubscriptionServiceAssignment, ServiceField, \
    SubscriptionServiceAssignmentField, ServiceFieldAssignment, SubscriptionAssignment


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionServiceAssignmentSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionServiceAssignment
        fields = '__all__'


class ServiceFieldSerializer(ModelSerializer):
    class Meta:
        model = ServiceField
        fields = '__all__'


class SubscriptionServiceAssignmentFieldSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionServiceAssignmentField
        fields = '__all__'


class ServiceFieldAssignmentSerializer(ModelSerializer):
    class Meta:
        model = ServiceFieldAssignment
        fields = '__all__'


class SubscriptionAssignmentSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionAssignment
        fields = '__all__'
