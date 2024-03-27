from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="admin@mail.ru",
            is_active=True,
            is_superuser=True,
            is_staff=True,
            password="111"
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """Test for creating user"""
        data = {
            "email": "test@mail.ru",
            "telegram_id": "@test",
            "password": "111"
        }

        response = self.client.post(
            '/users/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                "id": 8,
                "email": "test@mail.ru",
                "phone": None,
                "city": None,
                "avatar": None,
                "password": "111",
                "telegram_id": "@test",
                "chat_id": None,
            }
        )

    def test_users_list(self):
        """Test for display all users"""
        User.objects.create(
            email="test2@mail.ru",
            telegram_id="@test2",
            password="111",
        )

        response = self.client.get(
            '/users/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{
                "id": 15,
                "email": "admin@mail.ru",
                "phone": None,
                "city": None,
                "avatar": None,
                "password": "111",
                "telegram_id": "",
                "chat_id": None
            },
                {
                    "id": 16,
                    "email": "test2@mail.ru",
                    "phone": None,
                    "city": None,
                    "avatar": None,
                    "password": "111",
                    "telegram_id": "@test2",
                    "chat_id": None
                }
            ])

    def test_user_get(self):
        """Test for display one chosen user"""
        User.objects.create(
            email="test3@mail.ru",
            telegram_id="@test3",
            password="111",
        )

        response = self.client.get(
            '/users/14/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "id": 14,
                "email": "test3@mail.ru",
                "phone": None,
                "city": None,
                "avatar": None,
                "password": "111",
                "telegram_id": "@test3",
                "chat_id": None,
            }
        )

    def test_update_user(self):
        """Test for updating one chosen user"""
        data = {"email": "haha@mail.ru",
                "telegram_id": "@haha",
                "password": "111"
                }

        User.objects.create(
            email="test4@mail.ru",
            telegram_id="@test4",
            password="111",
        )

        response = self.client.patch(
            '/users/update/12/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "id": 12,
                "email": "haha@mail.ru",
                "phone": None,
                "city": None,
                "avatar": None,
                "password": "111",
                "telegram_id": "@haha",
                "chat_id": None,
            }
        )

    def test_delete_user(self):
        """Test for deleting one chosen user"""
        User.objects.create(
            email="test5@mail.ru",
            telegram_id="@test5",
            password="111",
        )

        response = self.client.delete(
            '/users/delete/10/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
