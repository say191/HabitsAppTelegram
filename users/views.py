from rest_framework.viewsets import generics
from users.serializers import UserSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from users.services import get_chat_id
from users.permissions import IsOwnerForUser


class UserCreateApiView(generics.CreateAPIView):
    """View for create user"""
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.chat_id = get_chat_id(user.telegram_id)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        password = serializer.data['password']
        user = User.objects.get(email=serializer.data['email'])
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListApiView(generics.ListAPIView):
    """User for display all users"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, ]


class UserRetrieveApiView(generics.RetrieveAPIView):
    """View for display one chosen user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerForUser | IsAdminUser, ]


class UserUpdateApiView(generics.UpdateAPIView):
    """View for update one chosen user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerForUser | IsAdminUser, ]


class UserDestroyApiView(generics.DestroyAPIView):
    """View for delete one chosen user"""
    queryset = User.objects.all()
    permission_classes = [IsOwnerForUser | IsAdminUser, ]
