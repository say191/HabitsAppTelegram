This is backend part of SPA Web app HabitsAppTelegram.
It include in a lot of tools from pack django.rest_framework.
There are two models (Habit and User), validators for different fields, paginator for simple displaying of data, permissions for each of endpoints,
endpoints like registration, authorization, list of owner's habits, list op public habits, creating habit, updating habit, deleting habit and other;
settings of CORS, tests and documentation.
Also a telegram bot is integrated into this app.
It sends notifications to habit's owner according to their settings.

Instructions:
IMPORTANT! Before registration on service you have to be sure, that your telegram account have @channelname. If you don't have @channelname, 
you need to create it in settings&
IMPORTANT! The next step is searhing @igor_baydikov_habit_bot in telegram. Then you have to press button start or something write to bot.
IMPORTANT! Without these steps the service cannot send you notifications in telegram.
After that you can register on service. There are three three required fields as email, password and telegram_id (@channelname).
Be careful, telegram_id must start with @.
After registration you can create your own habit.
For sending created habit you have to enter two commands in terminal: 
celery -A config beat -l INFO
celery -A config worker -l INFO
Also you need to be sure, that you installed all requirements from file named requirements.txt.

Periodic task runs every one minute via celery. Don't change settings for correct working service.
