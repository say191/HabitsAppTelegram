# Generated by Django 5.0.3 on 2024-03-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_chat_id_alter_user_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.CharField(default='without_bot', max_length=30, verbose_name='chat_id'),
        ),
    ]
