from django.urls import path
from .views import (
    AccountListView, AccountDetailView, CustomUserListView
)


urlpatterns = [
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('users/', CustomUserListView.as_view(), name='custom-user-list'),
]
