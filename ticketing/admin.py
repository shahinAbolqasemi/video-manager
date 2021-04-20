from django.contrib.admin import ModelAdmin, site
from .models import TicketCategory, Priority, TicketStatus, Ticket, TicketMessage, TicketFileAttachment, TicketComment, TicketCategoryUserAssignment, TicketCategoryReferRequest, UserReferRequest


class TicketCategoryAdmin(ModelAdmin):
    list_display = ['pk', 'title', 'related_creator', 'created_date', 'modified_date']

class PriorityAdmin(ModelAdmin):
    list_display = ['pk', 'title', 'related_creator', 'created_date', 'modified_date']

class TicketStatusAdmin(ModelAdmin):
    list_display = ['pk', 'title']

class TicketAdmin(ModelAdmin):
    list_display = ['pk', 'subject', 'related_priority', 'related_ticket_category', 'related_subscription']

class TicketMessageAdmin(ModelAdmin):
    list_display = ['pk', 'related_ticket']

class TicketFileAttachmentAdmin(ModelAdmin):
    list_display = ['pk', 'related_ticket_message', 'file']

class TicketCommentAdmin(ModelAdmin):
    list_display = ['pk', 'related_ticket', 'text']

class TicketCategoryUserAssignmentAdmin(ModelAdmin):
    list_display = ['pk', 'related_ticket_category', 'related_user', 'related_creator']

class TicketCategoryReferRequestAdmin(ModelAdmin):
    list_display = ['pk', 'related_ticket', 'related_ticket_category', 'related_creator']

class UserReferRequestAdmin(ModelAdmin):
    list_display = ['pk', 'related_ticket', 'related_user', 'related_creator']


site.register(TicketCategory, TicketCategoryAdmin)
site.register(Priority, PriorityAdmin)
site.register(TicketStatus, TicketStatusAdmin)
site.register(Ticket, TicketAdmin)
site.register(TicketMessage, TicketMessageAdmin)
site.register(TicketFileAttachment, TicketFileAttachmentAdmin)
site.register(TicketComment, TicketCommentAdmin)
site.register(TicketCategoryUserAssignment, TicketCategoryUserAssignmentAdmin)
site.register(TicketCategoryReferRequest, TicketCategoryReferRequestAdmin)
site.register(UserReferRequest, UserReferRequestAdmin)
