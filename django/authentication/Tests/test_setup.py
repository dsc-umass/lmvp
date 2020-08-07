from rest_framework.test import APITestCase
from django.urls import reverse

#Reverse takes in a view name and gives us a path to the route
class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.register_url = reverse('login')

        self.user_data= {
            'email':"new_test@gmail.com",
            'username':"testemail",
            'password':"Password1",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()




