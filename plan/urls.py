from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ServiceViewSet, SubscriptionViewSet, SubscriptionServiceAssignmentViewSet, ServiceFieldViewSet, SubscriptionServiceAssignmentFieldViewSet


router = SimpleRouter()
router.register(r'services', ServiceViewSet)
router.register(r'subscription', SubscriptionViewSet)
router.register(r'subscription-service-assignments', SubscriptionServiceAssignmentViewSet)
router.register(r'service-fields', ServiceFieldViewSet)
router.register(r'subscription-service-assignment-fields', SubscriptionServiceAssignmentFieldViewSet)


urlpatterns = router.urls
