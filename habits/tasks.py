from config.settings import TELEGRAM_API_KEY
import requests
from celery import shared_task
from habits.models import Habit
import datetime as d


@shared_task
def send_notification():
    """Shared task for send reminder notifications to habit's owner via telegram bot.
     This task iterate all created habits and then create time trigger for each of habits.
     Time trigger is one hour before the start of habit's action. It equals habit's start date
     plus start time minus one hour.
     Then by condition if time is equal to time trigger, task changes habit's start date to
     start date plus periodicity for correct sending the next notification.
     Also if habit's owner has chat_id (see ReadMe file) task send notification to habit's owner.
     According to settings this task runs every minute.
     Don't change celery settings for correct working this service"""
    habits = Habit.objects.all()
    for habit in habits:
        time_trigger = d.datetime.combine(habit.start_date, habit.start_time) - d.timedelta(hours=1)
        if d.datetime.now().replace(second=0, microsecond=0) == time_trigger.replace(second=0):
            if habit.owner.chat_id is not None:
                message = f"Don't forgive to {habit.action} in {habit.place} at {habit.start_time}"
                requests.get(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={habit.owner.chat_id}&text={message}")
            habit.start_date += d.timedelta(days=habit.get_periodicity_display())
            habit.save()
