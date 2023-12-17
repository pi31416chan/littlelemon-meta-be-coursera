from collections import OrderedDict

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Menu


class TestMenuView(TestCase):
    ANSWER = [
        OrderedDict(
            [
                ("id", 2),
                ("title", "IceCream"),
                ("price", "80.00"),
                ("inventory", 100),
            ]
        ),
        OrderedDict(
            [
                ("id", 3),
                ("title", "Pancake"),
                ("price", "30.00"),
                ("inventory", 20),
            ]
        ),
        OrderedDict(
            [
                ("id", 4),
                ("title", "Coke"),
                ("price", "2.00"),
                ("inventory", 6),
            ]
        ),
    ]

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = User(username="testuser", email="testuser@mail.com")
        cls.user.save()
        return super().setUpClass()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pancake", price=30, inventory=20)
        Menu.objects.create(title="Coke", price=2, inventory=6)
        return super().setUp()

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.data, self.ANSWER)
