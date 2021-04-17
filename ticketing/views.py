from django.shortcuts import render
from base.views import BaseViewSet
from .models import TicketCategory, TicketStatus, Ticket, TicketMessage, TicketFileAttachment, TicketComment, TicketCategoryUserAssignment, TicketCategoryReferRequest, UserReferRequest
from .serializers import TicketCategorySerializer, TicketStatusSerializer, TicketSerializer, TicketMessageSerializer, TicketFileAttachmentSerializer, TicketCommentSerializer, TicketCategoryUserAssignmentSerializer, TicketCategoryReferRequestSerializer, UserReferRequestSerializer


class TicketCategoryViewSet(BaseViewSet):
    queryset = TicketCategory.objects.all()
    serializer_class = TicketCategorySerializer


class TicketStatusViewSet(BaseViewSet):
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer


class TicketViewSet(BaseViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketMessageViewSet(BaseViewSet):
    queryset = TicketMessage.objects.all()
    serializer_class = TicketMessageSerializer


class TicketFileAttachmentViewSet(BaseViewSet):
    queryset = TicketFileAttachment.objects.all()
    serializer_class = TicketFileAttachmentSerializer


class TicketCommentViewSet(BaseViewSet):
    queryset = TicketComment.objects.all()
    serializer_class = TicketCommentSerializer


class TicketCategoryUserAssignmentViewSet(BaseViewSet):
    queryset = TicketCategoryUserAssignment.objects.all()
    serializer_class = TicketCategoryUserAssignmentSerializer


class TicketCategoryReferRequestViewSet(BaseViewSet):
    queryset = TicketCategoryReferRequest.objects.all()
    serializer_class = TicketCategoryReferRequestSerializer


class UserReferRequestViewSet(BaseViewSet):
    queryset = UserReferRequest.objects.all()
    serializer_class = UserReferRequestSerializer
