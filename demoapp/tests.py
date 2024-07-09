from django.test import TestCase
from datetime import datetime
from django.urls import reverse
from django.templatetags.static import static
from .models import Menu, Reservation

# Create your tests here.
class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Mocha", price=5)
        Menu.objects.create(name="Water", price=0)

    def test_menu_items(self):
        mocha = Menu.objects.get(name="Mocha")
        water = Menu.objects.get(name="Water")
        self.assertEqual(mocha.price, 5)
        self.assertEqual(water.price, 0)

    def test_menu_image(self):
        response = self.client.get(reverse('menu'))
        expected_url = static('img/dessert.jpg')
        self.assertIn(expected_url.encode(), response.content)

class ReservationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            first_name="John",
            last_name="Randolph"
        )
    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)