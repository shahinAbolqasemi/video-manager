from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer

from .mixins import RequestLogViewMixin


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BaseViewSet(ModelViewSet):
    def perform_create(self, serializer):
        if self.request.user:
            print(self.request.user)
            return serializer.save(creator_id=self.request.user.id, is_active=True)
        else:
            return serializer.save(creator=None, is_active=True)


def index(request):
    return HttpResponse("Video Cake Manager")
