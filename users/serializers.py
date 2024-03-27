from rest_framework import serializers
from users.models import User
from users.validators import TelegramValidator


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user's views """
    validators = [TelegramValidator(field='telegram_id'), ]

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city', 'avatar', 'password', 'telegram_id', 'chat_id')
