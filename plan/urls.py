from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ServiceViewSet, SubscriptionViewSet, SubscriptionServiceAssignmentViewSet, ServiceFieldViewSet, \
    SubscriptionServiceAssignmentFieldViewSet, ServiceFieldAssignmentViewSet, SubscriptionAssignmentViewSet

router = SimpleRouter()
router.register(r'services', ServiceViewSet)
router.register(r'subscription', SubscriptionViewSet)
router.register(r'subscription-service-assignments', SubscriptionServiceAssignmentViewSet)
router.register(r'service-fields', ServiceFieldViewSet)
router.register(r'subscription-service-assignment-fields', SubscriptionServiceAssignmentFieldViewSet)
router.register(r'service-field-assignments', ServiceFieldAssignmentViewSet)
router.register(r'subscription-assignments', SubscriptionAssignmentViewSet)

urlpatterns = router.urls
