from rest_framework import serializers
from finance_app.models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'date', 'description']

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount cannot be negative")
        elif value > 10000:
            raise serializers.ValidationError("Amount cannot be greater than 10,000")
        return value


class TransactionOutputSerializer(serializers.ModelSerializer):
    date_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'date_formatted', 'description']

    def get_date_formatted(self, obj):
        return obj.date.strftime("%d-%m-%Y %H:%M")
