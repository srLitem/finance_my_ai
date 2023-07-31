from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.models import Account,  CustomUser
from users.serializers import AccountSerializer, CustomUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class AccountListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        transactions_min_amount = request.GET.get('transactions_min_amount')

        if transactions_min_amount is not None:
            accounts = Account.objects.filter(user=request.user, accounts_key__amount__gt=float(transactions_min_amount)).distinct()
        else:
            accounts = Account.objects.filter(user=request.user)

        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, pk):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    @staticmethod
    def put(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomUserListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
