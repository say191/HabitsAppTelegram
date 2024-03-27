from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from habits.models import Habit


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="me@mail.ru",
            is_active=True
        )
        self.user.set_password("111")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Test for creating a habit"""
        data = {
            "place": "home",
            "start_date": "2024-04-01",
            "start_time": "11:00:00",
            "action": "read a book",
            "is_pleasant_habit": "False",
            "periodicity": "once_every_five_days",
            "reward": "knowledge",
            "time_done_in_sec": 100,
            "is_published": "True"
        }

        response = self.client.post(
            '/habits/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                "id": 1,
                "place": "home",
                "start_date": "2024-04-01",
                "start_time": "11:00:00",
                "action": "read a book",
                "is_pleasant_habit": False,
                "periodicity": "once_every_five_days",
                "reward": "knowledge",
                "time_done_in_sec": 100,
                "is_published": True,
                "owner": 1,
                "related_habit": None
            }
        )

    def test_published_habits_list(self):
        """Test for display published habits"""
        Habit.objects.create(
            place="home",
            start_date="2024-04-01",
            start_time="11:00:00",
            action="read a book",
            is_pleasant_habit="False",
            periodicity="once_every_five_days",
            reward="knowledge",
            time_done_in_sec=100,
            is_published="True",
            owner=self.user
        )
        response = self.client.get(
            '/habits/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{
                "id": 5,
                "place": "home",
                "start_date": "2024-04-01",
                "start_time": "11:00:00",
                "action": "read a book",
                "is_pleasant_habit": False,
                "periodicity": "once_every_five_days",
                "reward": "knowledge",
                "time_done_in_sec": 100,
                "is_published": True,
                "owner": 5,
                "related_habit": None
            }]
        )

    def test_owner_habits_list(self):
        """Test for display owner's habits"""
        Habit.objects.create(
            place="home",
            start_date="2024-04-01",
            start_time="11:00:00",
            action="read a book",
            is_pleasant_habit="False",
            periodicity="once_every_five_days",
            reward="knowledge",
            time_done_in_sec=100,
            is_published="True",
            owner=self.user
        )
        response = self.client.get(
            '/habits/my_habits/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results":
                    [{
                        "id": 4,
                        "place": "home",
                        "start_date": "2024-04-01",
                        "start_time": "11:00:00",
                        "action": "read a book",
                        "is_pleasant_habit": False,
                        "periodicity": "once_every_five_days",
                        "reward": "knowledge",
                        "time_done_in_sec": 100,
                        "is_published": True,
                        "owner": 4,
                        "related_habit": None
                    }]
            }
        )

    def test_habit_get(self):
        """Test for display one chosen habit"""
        Habit.objects.create(
            place="home",
            start_date="2024-04-01",
            start_time="11:00:00",
            action="read a book",
            is_pleasant_habit="False",
            periodicity="once_every_five_days",
            reward="knowledge",
            time_done_in_sec=100,
            is_published="True",
            owner=self.user
        )

        response = self.client.get(
            '/habits/3/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "id": 3,
                "place": "home",
                "start_date": "2024-04-01",
                "start_time": "11:00:00",
                "action": "read a book",
                "is_pleasant_habit": False,
                "periodicity": "once_every_five_days",
                "reward": "knowledge",
                "time_done_in_sec": 100,
                "is_published": True,
                "owner": 3,
                "related_habit": None
            }
        )

    def test_update_habit(self):
        """Test for updating one chosen habit"""
        data = {"place": "test",
                "start_date": "2024-04-01",
                "start_time": "11:00:00",
                "action": "read a book",
                "is_pleasant_habit": "False",
                "periodicity": "once_every_five_days",
                "reward": "knowledge",
                "time_done_in_sec": 100,
                "is_published": "True"
                }

        Habit.objects.create(
            place="home",
            start_date="2024-04-01",
            start_time="11:00:00",
            action="read a book",
            is_pleasant_habit="False",
            periodicity="once_every_five_days",
            reward="knowledge",
            time_done_in_sec=100,
            is_published="True",
            owner=self.user
        )

        response = self.client.patch(
            '/habits/update/6/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "id": 6,
                "place": "test",
                "start_date": "2024-04-01",
                "start_time": "11:00:00",
                "action": "read a book",
                "is_pleasant_habit": False,
                "periodicity": "once_every_five_days",
                "reward": "knowledge",
                "time_done_in_sec": 100,
                "is_published": True,
                "owner": 6,
                "related_habit": None
            }
        )

    def test_delete_habit(self):
        """Test for deleting one chosen habit"""
        Habit.objects.create(
            place="home",
            start_date="2024-04-01",
            start_time="11:00:00",
            action="read a book",
            is_pleasant_habit="False",
            periodicity="once_every_five_days",
            reward="knowledge",
            time_done_in_sec=100,
            is_published="True",
            owner=self.user
        )

        response = self.client.delete(
            '/habits/delete/2/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
