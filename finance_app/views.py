from django.shortcuts import render
from finance_app.models import Account, Category, Transaction
from finance_app.serializers import AccountSerializer, CategorySerializer, TransactionSerializer
from rest_framework import generics


# Create your views here.
class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = TransactionSerializer
