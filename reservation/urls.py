from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, ParticipantViewSet, ParticipantAssignmentViewSet, \
    SessionRequestServiceFieldAssignmentViewSet

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet, basename='session_request')
router.register(r'participants', ParticipantViewSet, basename='participants')
router.register(r'participant-assignments', ParticipantAssignmentViewSet, basename='participant_assignments')
router.register(r'session-request-service-field-assignments', SessionRequestServiceFieldAssignmentViewSet,
                basename='session_request_service_field_assignment')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
