from rest_framework.serializers import ValidationError


class TelegramValidator:
    """Validator for field named telegram_id"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        telegram_id = value.get(self.field)
        if telegram_id[0] != '@':
            raise ValidationError('Telegram id starts with @!')
