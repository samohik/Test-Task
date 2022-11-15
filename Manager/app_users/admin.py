from django.contrib import admin
from app_users.models import Profile, Category, TransactionHistory


@admin.register(Profile)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'balance', ]


@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(TransactionHistory)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'amount', 'time', 'category', 'organization', 'description',
    ]
