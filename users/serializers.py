from rest_framework import serializers
from users.models import Account, CustomUser


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'name', 'balance']
        extra_kwargs = {
            'name': {'required': False}
        }

    def validate_name(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("The name can not have more than 10 characters")
        return value

    def create(self, validated_data):
        name = validated_data.get('name')
        if name is None:
            validated_data['name'] = 'Default Name'
        account = super().create(validated_data)
        if name is None:
            account.name = 'Account_' + str(account.id)
            account.save()
        return account


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']