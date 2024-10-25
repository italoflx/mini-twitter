from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()  # Para listar seguidores

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'followers_count', 'followers']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def get_followers(self, obj):
        return [{"id": follower.id, "username": follower.username, "email": follower.email} for follower in obj.followers.all()]
