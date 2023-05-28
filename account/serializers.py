from rest_framework import serializers

from .models import User, FriendshipRequest


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'friends_count', 'posts_count', 'get_avatar', 'is_active', 'date_joined', 'last_login')
        read_only_field = ['is_active']


class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)