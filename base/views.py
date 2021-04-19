from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserAdminSerializer, UserSchedulerSerializer, UserCustomerSerializer
from . import permissions
from rest_framework import permissions as base_permissions
from .mixins import RequestLogViewMixin


class UserViewSet(ModelViewSet):
    """
    This ViewSet is for User model
    but with permissions
    """
    serializer_class = UserCustomerSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [
        base_permissions.IsAuthenticated,
        permissions.IsAdminOrModifyOnly,
    ]

    def get_serializer_class(self):
        """
        This method set serializer to:
        UserAdminSerializer if user is admin
        UserSchedulerSerializer if user is scheduler
        else -> default serializer that is UserCustomerSerializer
        """
        if self.request.user.is_superuser:
            return UserAdminSerializer
        elif self.request.user.check_group('scheduler'):
            return UserSchedulerSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        """
        This method return queryset.
        if user is customer queryset limited to your self user account
        else -> return default queryset that is (UserModel).objects.all()
        """
        if self.request.user.check_group('customer'):
            return get_user_model().objects.filter(id=self.request.user.id)
        return super().get_queryset()


class BaseViewSet(ModelViewSet):
    def perform_create(self, serializer):
        if self.request.user:
            print(self.request.user)
            return serializer.save(creator_id=self.request.user.id, is_active=True)
        else:
            return serializer.save(creator=None, is_active=True)


def index(request):
    return HttpResponse("Video Cake Manager")
