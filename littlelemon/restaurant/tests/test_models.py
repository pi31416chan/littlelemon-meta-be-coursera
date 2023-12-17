from django.test import TestCase

from ..models import Menu


class TestMenu(TestCase):
    def test_create_menu(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
