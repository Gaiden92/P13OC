from django.test import TestCase
from django.test import Client

from .models import Profile, User


class TestProfile(TestCase):

    def setUp(self) -> None:

        self.data = {
                "username": "Test",
                "password": "hello",
                "email" : "test@hotmail.fr",
                "first_name" : "Test Firstname",
                "last_name" : "Test Lastname",
        }
        self.favorite_city = "Suresnes"

        self.user = User.objects.create_user(**self.data)

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city=self.favorite_city)
         
    def test_profile(self):
        self.assertEqual(self.profile.user, self.user)

    def test_profile_favorite_city(self):
        self.favorite_city = "Madrid"
        self.assertNotEqual(self.profile.favorite_city, self.favorite_city)

# Test index view
class TestIndexView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.profiles_list = Profile.objects.all()
        self.response = self.client.get('/')

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

# Test index view
class TestProfileView(TestCase):
    def setUp(self) -> None:
        self.data = {
                "username": "Test",
                "password": "hello",
                "email" : "test@hotmail.fr",
                "first_name" : "Test Firstname",
                "last_name" : "Test Lastname",
        }
        self.user = User.objects.create_user(**self.data)

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Rueil")
        self.client = Client()
        self.response = self.client.get(f'/profiles/{self.user.username}/')

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'profiles/profile.html')

# Test index view
class TestProfilesView(TestCase):
    def setUp(self) -> None:
        self.data = {
                "username": "Test",
                "password": "hello",
                "email" : "test@hotmail.fr",
                "first_name" : "Test Firstname",
                "last_name" : "Test Lastname",
        }
        self.user = User.objects.create_user(**self.data)

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Rueil")
        self.client = Client()
        self.response = self.client.get(f'/profiles/')

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'profiles/index.html')