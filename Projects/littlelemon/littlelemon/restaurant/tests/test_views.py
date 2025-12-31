from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pasta", price=12.50, inventory=20)
        Menu.objects.create(title="Salad", price=8.00, inventory=35)
        Menu.objects.create(title="Soup", price=6.25, inventory=15)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)
