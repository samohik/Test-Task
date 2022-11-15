from django.urls import path, include
from rest_framework import routers

from app_users.views import ProfileViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('v1/drf-auth/', include('rest_framework.urls')),
    path('v1/', include(router.urls)),
    # path to djoser end points
    path('v1/auth/', include('djoser.urls')),
]
