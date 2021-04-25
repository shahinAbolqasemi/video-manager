from django.shortcuts import render
from base.views import BaseViewSet, BaseReadOnlyViewSet
from .models import TicketCategory, TicketStatus, Ticket, TicketMessage, TicketFileAttachment, TicketComment, \
    TicketCategoryUserAssignment, TicketCategoryReferRequest, UserReferRequest, Priority
from .serializers import TicketCategorySerializer, TicketStatusSerializer, TicketSerializer, TicketMessageSerializer, \
    TicketFileAttachmentSerializer, TicketCommentSerializer, TicketCategoryUserAssignmentSerializer, \
    TicketCategoryReferRequestSerializer, UserReferRequestSerializer, PrioritySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class TicketCategoryViewSet(BaseViewSet):
    queryset = TicketCategory.objects.all()
    serializer_class = TicketCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class TicketStatusViewSet(BaseViewSet):
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class TicketViewSet(BaseViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['subject', 'related_priority', 'related_ticket_category', 'related_subscription',
                        'related_ticket_status', 'referred_to_ticket_category', 'referred_to_user']
    search_fields = ['subject']

    def get_queryset(self):
        user_ticket_categories = TicketCategory.objects.filter(ticketcategoryuserassignment__related_user=self.request.user)
        if self.request.user.is_authenticated:
            return Ticket.objects.filter(referred_to_ticket_category__in=user_ticket_categories)
        return super().get_queryset()


class TicketMessageViewSet(BaseViewSet):
    queryset = TicketMessage.objects.all()
    serializer_class = TicketMessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_ticket']


class TicketFileAttachmentViewSet(BaseViewSet):
    queryset = TicketFileAttachment.objects.all()
    serializer_class = TicketFileAttachmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_ticket_message']


class TicketCommentViewSet(BaseViewSet):
    queryset = TicketComment.objects.all()
    serializer_class = TicketCommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_ticket']


class TicketCategoryUserAssignmentViewSet(BaseViewSet):
    queryset = TicketCategoryUserAssignment.objects.all()
    serializer_class = TicketCategoryUserAssignmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_ticket_category', 'related_user']


class TicketCategoryReferRequestViewSet(BaseViewSet):
    queryset = TicketCategoryReferRequest.objects.all()
    serializer_class = TicketCategoryReferRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_ticket', 'related_ticket_category']


class UserReferRequestViewSet(BaseViewSet):
    queryset = UserReferRequest.objects.all()
    serializer_class = UserReferRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_ticket', 'related_user']


class PriorityViewSet(BaseReadOnlyViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
