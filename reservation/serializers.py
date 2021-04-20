from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from reservation.models import Participant, ParticipantAssignment, ServiceRequest


class ParticipantSerializer(serializers.ModelSerializer):
    """
    This serializer is for Participant model
    """
    related_creator = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Participant
        fields = '__all__'


class ParticipantAssignmentSerializer(serializers.ModelSerializer):
    """
    This serializer is for ParticipantAssignment model
    """
    related_creator = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ParticipantAssignment
        fields = '__all__'


class ServiceRequestAdminSerializer(serializers.ModelSerializer):
    """
    The serializer for ServiceRequest model for admin
    """
    related_creator = serializers.PrimaryKeyRelatedField(read_only=True)
    related_customer = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.filter(groups__name='customer'),
        label='Customer'
    )
    unique_id = serializers.ReadOnlyField()
    related_participants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ServiceRequest
        fields = '__all__'


class ServiceRequestSchedulerSerializer(serializers.ModelSerializer):
    """
    The serializer for ServiceRequest model for scheduler
    """
    related_creator = serializers.PrimaryKeyRelatedField(read_only=True)
    related_customer = serializers.PrimaryKeyRelatedField(read_only=True)
    nodes_count = serializers.ReadOnlyField()
    groups_count = serializers.ReadOnlyField()
    unique_id = serializers.ReadOnlyField()
    start_date = serializers.ReadOnlyField()
    end_date = serializers.ReadOnlyField()
    related_participants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ServiceRequest
        fields = '__all__'


class ServiceRequestCustomerSerializer(serializers.ModelSerializer):
    """
    The serializer for ServiceRequest model for customer
    """

    class Meta:
        model = ServiceRequest
        fields = [
            'id',
            'unique_id',
            'is_accepted',
            'nodes_count',
            'groups_count',
            'start_date',
            'end_date',
        ]
