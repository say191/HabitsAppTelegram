# Generated by Django 5.0.3 on 2024-03-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(default='without_bot', max_length=30, unique=True, verbose_name='telegram_id'),
        ),
    ]
