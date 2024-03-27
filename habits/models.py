from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIODICITY = (
        ('once_a_day', 1),
        ('once_every_two_days', 2),
        ('once_every_three_days', 3),
        ('once_every_four_days', 4),
        ('once_every_five_days', 5),
        ('once_every_six_days', 6),
        ('once_a_week', 7),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='place')
    start_date = models.DateField(verbose_name='start_date', **NULLABLE)
    start_time = models.TimeField(verbose_name='start_time', default='09:00:00')
    action = models.CharField(max_length=50, verbose_name='action')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name='is_pleasant_habit')
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='related_habit', **NULLABLE)
    periodicity = models.CharField(choices=PERIODICITY, verbose_name='periodicity', default='once_a_day')
    reward = models.CharField(max_length=50, verbose_name='reward', **NULLABLE)
    time_done_in_sec = models.PositiveIntegerField(verbose_name='time_done_in_sec', default=120)
    is_published = models.BooleanField(default=False, verbose_name='is_published')

    def __str__(self):
        return f"I will {self.action} at {self.start_time} in {self.place} {self.periodicity}"

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
