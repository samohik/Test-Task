from rest_framework import serializers
from app_users.models import Profile, TransactionHistory


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'balance',
        ]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = [
            'amount', 'time', 'category',
            'organization', 'description',
        ]
