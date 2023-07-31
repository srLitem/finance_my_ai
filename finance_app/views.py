from django.shortcuts import get_object_or_404
from finance_app.models import Category, Transaction
from finance_app.serializers import CategorySerializer, TransactionSerializer, TransactionOutputSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.db.models import Sum


from django.db.models import Exists, OuterRef

from users.models import Account


class CategoryListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        amount_min = request.GET.get('amount_min')
        amount_max = request.GET.get('amount_max')
        date_min = request.GET.get('date_min')
        date_max = request.GET.get('date_max')

        transactions = Transaction.objects.all()

        if amount_min is not None:
            transactions = transactions.filter(amount__gte=float(amount_min))
        if amount_max is not None:
            transactions = transactions.filter(amount__lte=float(amount_max))
        if date_min is not None:
            transactions = transactions.filter(date__gte=date_min)
        if date_max is not None:
            transactions = transactions.filter(date__lte=date_max)

        serializer = TransactionOutputSerializer(transactions, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            account_id = request.data.get('account')
            category_id = request.data.get('category')

            account = Account.objects.get(pk=account_id)
            category = Category.objects.get(pk=category_id)

            serializer.save(account=account, category=category)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailView(APIView):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)