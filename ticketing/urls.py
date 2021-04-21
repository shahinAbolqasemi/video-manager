from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TicketCategoryViewSet, TicketStatusViewSet, TicketViewSet, TicketMessageViewSet, \
    TicketFileAttachmentViewSet, TicketCommentViewSet, TicketCategoryUserAssignmentViewSet, \
    TicketCategoryReferRequestViewSet, UserReferRequestViewSet, PriorityViewSet

router = SimpleRouter()
router.register(r'ticket-categories', TicketCategoryViewSet)
router.register(r'ticket-messages', TicketMessageViewSet)
router.register(r'ticket-file-attachments', TicketFileAttachmentViewSet)
router.register(r'ticket-statuses', TicketStatusViewSet)
router.register(r'ticket-comments', TicketCommentViewSet)
router.register(r'ticket-category-user-assignments', TicketCategoryUserAssignmentViewSet)
router.register(r'ticket-category-refer-requests', TicketCategoryReferRequestViewSet)
router.register(r'user-refer-requests', UserReferRequestViewSet)
router.register(r'priorities', PriorityViewSet)
router.register(r'', TicketViewSet)


urlpatterns = router.urls
