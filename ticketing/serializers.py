from rest_framework.serializers import ModelSerializer
from .models import TicketCategory, TicketStatus, Ticket, TicketMessage, TicketFileAttachment, TicketComment, \
    TicketCategoryUserAssignment, TicketCategoryReferRequest, UserReferRequest, Priority


class TicketCategorySerializer(ModelSerializer):
    class Meta:
        model = TicketCategory
        fields = '__all__'


class TicketStatusSerializer(ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketMessageSerializer(ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = '__all__'


class TicketFileAttachmentSerializer(ModelSerializer):
    class Meta:
        model = TicketFileAttachment
        fields = '__all__'


class TicketCommentSerializer(ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'


class TicketCategoryUserAssignmentSerializer(ModelSerializer):
    class Meta:
        model = TicketCategoryUserAssignment
        fields = '__all__'


class TicketCategoryReferRequestSerializer(ModelSerializer):
    class Meta:
        model = TicketCategoryReferRequest
        fields = '__all__'


class UserReferRequestSerializer(ModelSerializer):
    class Meta:
        model = UserReferRequest
        fields = '__all__'


class PrioritySerializer(ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'
