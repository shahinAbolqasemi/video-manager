from rest_framework.viewsets import ModelViewSet
from reservation.serializers import (
    SessionRequestSchedulerSerializer,
    SessionRequestAdminSerializer, SessionRequestCustomerSerializer, ParticipantSerializer,
    ParticipantAssignmentSerializer,
)
from base import permissions
from rest_framework import permissions as base_permissions
from .models import SessionRequest, Participant, ParticipantAssignment


class SessionRequestViewSet(ModelViewSet):
    """
    The view is for SessionRequest model
    """
    serializer_class = SessionRequestAdminSerializer
    queryset = SessionRequest.objects.all()
    permission_classes = [
        base_permissions.IsAuthenticated,
        permissions.IsAdminOrModifierSchedulerOrReadOnly,
    ]

    def get_serializer_class(self):
        """
        This method return serializer class as follows:
        if user is admin return SessionRequestAdminSerializer
        if user is scheduler return SessionRequestSchedulerSerializer
        if user is customer return SessionRequestCustomerSerializer
        """
        if self.request.user.is_superuser:
            return SessionRequestAdminSerializer
        elif self.request.user.check_group('scheduler'):
            return SessionRequestSchedulerSerializer
        elif self.request.user.check_group('customer'):
            return SessionRequestCustomerSerializer

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
            return SessionRequest.objects.filter(related_customer=self.request.user.id)
        return super().get_queryset()


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
