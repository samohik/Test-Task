from django.db import transaction

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app_users.models import TransactionHistory, Profile, Category
from app_users.serializers import ProfileSerializer, TransactionSerializer
from app_users.service import UserFilter, TransactionFilter


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = UserFilter

    @action(methods=['GET'], detail=True)
    def category(self, request, pk=None):
        if pk:
            category = Category.objects.filter(profile=pk)
            return Response({'category': [val.name for val in category]})


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TransactionFilter


def some_func():
    with transaction.atomic():
        ...
