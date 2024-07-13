from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Vanila',price=23,inventory=120)
        self.menu2 = Menu.objects.create(title='Chocolate',price=45,inventory=124)
        self.menu3 = Menu.objects.create(title='Strewberry',price=21,inventory=125)
        
    
    def test_getall(self):
        # Retrieve all menu items
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Assertions to check if the serialized data equals the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)