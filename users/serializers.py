from rest_framework import serializers
from users.models import Account, CustomUser


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'name', 'balance']

    def validate_name(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("The name can not have more than 10 characters")
        return value


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']