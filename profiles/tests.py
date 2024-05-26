from django.test import TestCase, Client
from django.urls import reverse

from .models import Profile, User
from profiles.apps import ProfilesConfig


class TestProfile(TestCase):
    """Class for testing the Profile model."""
    def setUp(self):
        """Initialization of data for tests."""
        self.data = {
            "username": "Test",
            "password": "hello",
            "email": "test@hotmail.fr",
            "first_name": "Test Firstname",
            "last_name": "Test Lastname",
        }
        self.favorite_city = "Suresnes"
        self.user = User.objects.create_user(**self.data)
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city=self.favorite_city
        )

    def test_profile(self):
        """Method to test the association between profile and user."""
        self.assertEqual(self.profile.user, self.user)

    def test_profile_favorite_city(self):
        """Method to test favorite city in the profile."""
        self.assertNotEqual(self.profile.favorite_city, "Madrid")


class TestIndexView(TestCase):
    """Class for testing the index view."""
    def setUp(self):
        """Initialization of data for tests."""
        self.client = Client()
        self.profiles_list = Profile.objects.all()
        self.response = self.client.get('/')

    def test_response(self):
        """Method to test the response of the view."""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Method to test the template used."""
        self.assertTemplateUsed(self.response, 'index.html')


class TestProfileView(TestCase):
    """Class for testing the profile view."""
    def setUp(self):
        """Initialization of data for tests."""
        self.data = {
            "username": "Test",
            "password": "hello",
            "email": "test@hotmail.fr",
            "first_name": "Test Firstname",
            "last_name": "Test Lastname",
        }
        self.user = User.objects.create_user(**self.data)
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Rueil"
        )
        self.client = Client()
        self.response = self.client.get(f'/profiles/{self.user.username}/')

    def test_response(self):
        """Method to test the response of the view."""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Method to test the template used."""
        self.assertTemplateUsed(self.response, 'profiles/profile.html')


class TestProfilesView(TestCase):
    """Class for testing the profiles view."""
    def setUp(self):
        """Initialization of data for tests."""
        self.data = {
            "username": "Test",
            "password": "hello",
            "email": "test@hotmail.fr",
            "first_name": "Test Firstname",
            "last_name": "Test Lastname",
        }
        self.user = User.objects.create_user(**self.data)
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Rueil"
        )
        self.client = Client()
        self.response = self.client.get(f'/profiles/')

    def test_profile_view_nonexistent_user(self):
        """Method to test redirection for nonexistent user."""
        response = self.client.get(reverse('profile', args=['nonexistentuser']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profiles_index'))

    def test_profile_view(self):
        """Method to test profile view."""
        response = self.client.get(reverse('profile', args=['Test']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_response(self):
        """Method to test the response of the view."""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Method to test the template used."""
        self.assertTemplateUsed(self.response, 'profiles/index.html')


class ProfilesURLTests(TestCase):
    """Class for testing profile URLs."""
    def setUp(self):
        """Initialization of data for tests."""
        self.client = Client()

    def test_profiles_index_url(self):
        """Method to test the profiles index URL."""
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)

    def test_profile_url_with_valid_username(self):
        """Method to test profile URL with valid username."""
        username = 'testuser'
        response = self.client.get(reverse('profile', args=[username]))
        self.assertEqual(response.status_code, 302)

    def test_profile_url_with_invalid_username(self):
        """Method to test profile URL with invalid username."""
        username = 9
        response = self.client.get(reverse('profile', args=[username]))
        self.assertEqual(response.status_code, 302)


class ProfilesConfigTest(TestCase):
    """Class for testing the profiles application configuration."""
    def test_app_config(self):
        """Method to test the configuration of the profiles application."""
        self.assertEqual(ProfilesConfig.name, 'profiles')
