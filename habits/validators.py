from rest_framework.serializers import ValidationError


class TimeValidator:
    """Validator for field named time_done_in_sec"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_done_in_sec = value.get(self.field)
        if time_done_in_sec > 120:
            raise ValidationError('Time for managing this habit must be no more than 120 sec')


class RewardValidator:
    """Validator for fields named related habit and reward.
    We cannot get both pleasant habit and reward for completing a habit's action.
     Choose only one: related (pleasant habit) or reward"""
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = value.get(self.field1)
        reward = value.get(self.field2)
        if related_habit is not None:
            if reward is not None:
                raise ValidationError('You must choice only related_habit or only reward')


class RelatedHabitValidator:
    """Validator for field named related habit.
    You cannot point habit with pleasant attribute (is_pleasant_habit) as related habit"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field):
            related_habit = value.get(self.field)
            if not related_habit.is_pleasant_habit:
                raise ValidationError("You can't choice this habit as related habit")


class PleasantHabitValidator:
    """Validator not to select pleasant habit or reward for completing action of pleasant habit"""
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = value.get(self.field1)
        reward = value.get(self.field2)
        is_pleasant_habit = value.get(self.field3)
        if related_habit or reward:
            if is_pleasant_habit:
                raise ValidationError("You can't get reward or related_habit for pleasant_habit")
