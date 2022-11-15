from django_filters import rest_framework as filters
from app_users.models import Profile, TransactionHistory


class UserFilter(filters.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'id': ['exact', ],
            'balance': ['lt', 'gt', ],
        }


class TransactionFilter(filters.FilterSet):
    class Meta:
        model = TransactionHistory
        fields = {
            'amount': ['exact', 'lt', 'gt', ],
            'time': ['year__gt', 'year__lt', ],
            'category': ['exact', 'contains', ],
            'organization': ['exact', ],
        }
