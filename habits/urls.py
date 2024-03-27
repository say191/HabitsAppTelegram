from habits.apps import HabitsConfig
from django.urls import path
from habits import views

app_name = HabitsConfig.name

urlpatterns = [
    path('', views.PublishedHabitListApiView.as_view(), name='published_habits_list'),
    path('my_habits/', views.HabitListApiView.as_view(), name='my_habits_list'),
    path('create/', views.HabitCreateApiView.as_view(), name='habits_create'),
    path('<int:pk>/', views.HabitRetrieveApiView.as_view(), name='habits_get'),
    path('update/<int:pk>/', views.HabitUpdateApiView.as_view(), name='habits_update'),
    path('delete/<int:pk>/', views.HabitDestroyApiView.as_view(), name='habits_delete'),
]
