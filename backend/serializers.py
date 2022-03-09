from rest_framework import serializers
from rest_framework.authtoken.admin import User

from backend.models import GuestBook


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class GuestBookSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        created_at = obj.created_at.strftime("%d/%m/%Y - %H:%M:%S")
        return created_at

    class Meta:
        model = GuestBook
        fields = "__all__"
