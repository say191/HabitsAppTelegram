from users.apps import UsersConfig
from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('', views.UserListApiView.as_view(), name='users_list'),
    path('create/', views.UserCreateApiView.as_view(), name='users_register'),
    path('<int:pk>/', views.UserRetrieveApiView.as_view(), name='users_get'),
    path('update/<int:pk>/', views.UserUpdateApiView.as_view(), name='users_update'),
    path('delete/<int:pk>/', views.UserDestroyApiView.as_view(), name='users_delete'),
    path('token/', TokenObtainPairView.as_view(), name='users_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
