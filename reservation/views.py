from rest_framework.viewsets import ModelViewSet
from base.views import BaseViewSet
from plan.models import SubscriptionAssignment, ServiceField, SubscriptionServiceAssignmentField
from reservation.serializers import (
    ServiceRequestSchedulerSerializer,
    ServiceRequestAdminSerializer, ServiceRequestCustomerSerializer, ParticipantSerializer,
    ParticipantAssignmentSerializer, ServiceRequestServiceFieldAssignmentSerializer,
)
from base import permissions
from rest_framework import permissions as base_permissions
from .models import ServiceRequest, Participant, ParticipantAssignment, ServiceRequestServiceFieldAssignment
from rest_framework.response import Response
from rest_framework import status


class ServiceRequestViewSet(ModelViewSet):
    """
    The view is for ServiceRequest model
    """
    serializer_class = ServiceRequestAdminSerializer
    queryset = ServiceRequest.objects.all()
    permission_classes = [
        base_permissions.IsAuthenticated,
        permissions.IsAdminOrModifierSchedulerOrReadOnly,
    ]

    def get_serializer_class(self):
        """
        This method return serializer class as follows:
        if user is admin return ServiceRequestAdminSerializer
        if user is scheduler return ServiceRequestSchedulerSerializer
        if user is customer return ServiceRequestCustomerSerializer
        """
        if self.request.user.is_superuser:
            return ServiceRequestAdminSerializer
        elif self.request.user.check_group('scheduler'):
            return ServiceRequestSchedulerSerializer
        elif self.request.user.check_group('customer'):
            return ServiceRequestCustomerSerializer

    def perform_create(self, serializer):
        """
        This method is for add related_creator to data for perform create session request
        Here set to applicant user
        """
        serializer.save(related_creator=self.request.user)

    def get_queryset(self):
        """
        This method is for return queryset as follows:
        if user is customer return your self session requests queryset
        """
        if self.request.user.check_group('customer'):
            return ServiceRequest.objects.filter(related_customer=self.request.user.id)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        print(request.data.get('related_customer'))
        if SubscriptionAssignment.active.filter(related_customer=request.data.get('related_customer')).exists():
            return super().create(request, *args, **kwargs)
        else:
            content = {'error': 'nothing to see here'}
            return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)


class ParticipantViewSet(ModelViewSet):
    """
    This ViewSet is for Participant model
    """
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
    permission_classes = [
        base_permissions.IsAuthenticated,
        permissions.IsAdminOrReadOnly,
    ]

    def perform_create(self, serializer):
        """
        This method is for add related_creator to data for perform create session request
        Here set to applicant user
        """
        serializer.save(related_creator=self.request.user)


class ParticipantAssignmentViewSet(ModelViewSet):
    """
    This ViewSet is for ParticipantAssignment model
    """
    serializer_class = ParticipantAssignmentSerializer
    queryset = ParticipantAssignment.objects.all()
    permission_classes = [
        base_permissions.IsAuthenticated,
        permissions.IsAdminOrSchedulerViewer,
    ]

    def perform_create(self, serializer):
        """
        This method is for add related_creator to data for perform create session request
        Here set to applicant user
        """
        serializer.save(related_creator=self.request.user)


class ServiceRequestServiceFieldAssignmentViewSet(BaseViewSet):
    queryset = ServiceRequestServiceFieldAssignment.objects.all()
    serializer_class = ServiceRequestServiceFieldAssignmentSerializer

    def create(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        subscription_service_assignment_field = SubscriptionServiceAssignmentField.objects.filter(
            related_service_field=ServiceField.objects.get(id=request.data.get('related_service_field')))
        if SubscriptionAssignment.active.filter(
                related_customer=ServiceRequest.objects.get(id=request.data.get('related_service_request')).related_customer,
                related_subscription__subscriptionserviceassignment__subscriptionserviceassignmentfield__amount__gte=amount,
                related_subscription__subscriptionserviceassignment__subscriptionserviceassignmentfield__in=subscription_service_assignment_field,
                related_subscription__subscriptionserviceassignment__related_service_id=request.data.get('related_service')
        ).exists():
            return super().create(request, *args, **kwargs)
        else:
            content = {'error': 'nothing to see here'}
            return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)
