from rest_framework import serializers
from habits.models import Habit
from habits.validators import TimeValidator, RewardValidator, RelatedHabitValidator, PleasantHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Serializer for habit's views"""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [TimeValidator(field='time_done_in_sec'),
                      RewardValidator(field1='related_habit', field2='reward'),
                      RelatedHabitValidator(field='related_habit'),
                      PleasantHabitValidator(field1='related_habit', field2='reward', field3='is_pleasant_habit')]
