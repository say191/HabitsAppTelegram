# Generated by Django 5.0.3 on 2024-03-24 12:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='place')),
                ('time', models.TimeField(verbose_name='time')),
                ('action', models.CharField(max_length=50, verbose_name='action')),
                ('is_pleasant_habit', models.BooleanField(default=False, verbose_name='is_pleasant_habit')),
                ('periodicity', models.CharField(choices=[('once_a_day', 'once_a_day'), ('once_every_two_days', 'once_every_two_days'), ('once_every_three_days', 'once_every_three_days'), ('once_every_four_days', 'once_every_four_days'), ('once_every_five_days', 'once_every_five_days'), ('once_every_six_days', 'once_every_six_days'), ('once_a_week', 'once_a_week')], verbose_name='periodicity')),
                ('reward', models.CharField(blank=True, max_length=50, null=True, verbose_name='reward')),
                ('time_done', models.CharField(max_length=30, verbose_name='time_done')),
                ('is_published', models.BooleanField(default=True, verbose_name='is_published')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='related_habit')),
            ],
            options={
                'verbose_name': 'habit',
                'verbose_name_plural': 'habits',
            },
        ),
    ]
