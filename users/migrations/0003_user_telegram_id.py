# Generated by Django 5.0.3 on 2024-03-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_avatar_user_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='telegram_id'),
        ),
    ]
