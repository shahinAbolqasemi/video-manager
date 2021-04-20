from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserAdminSerializer(serializers.ModelSerializer):
    """
    This serializer is for Users with admin permission
    """
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class UserSchedulerSerializer(serializers.ModelSerializer):
    """
    This serializer is for Users with scheduler permission
    """
    date_joined = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()
    password = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_permissions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class UserCustomerSerializer(serializers.ModelSerializer):
    """
    This serializer is a customer serializer
    """

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]

