from rest_framework.viewsets import generics
from habits.serializers import HabitSerializer
from habits.models import Habit
from habits.paginators import HabitPaginator
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.permissions import IsOwnerForHabit
from datetime import date


class HabitCreateApiView(generics.CreateAPIView):
    """View for create a habit"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        if new_habit.start_date is None:
            new_habit.start_date = date.today()
        new_habit.save()


class HabitListApiView(generics.ListAPIView):
    """View for display list of owner's habits"""
    permission_classes = [IsAuthenticated, ]
    pagination_class = HabitPaginator
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class PublishedHabitListApiView(generics.ListAPIView):
    """View for display list of published habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    permission_classes = [IsAuthenticated, ]


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """View for display one chosen habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerForHabit | IsAdminUser, ]


class HabitUpdateApiView(generics.UpdateAPIView):
    """View for update one chosen habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerForHabit | IsAdminUser, ]


class HabitDestroyApiView(generics.DestroyAPIView):
    """View for delete one chosen habit"""
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerForHabit | IsAdminUser, ]
