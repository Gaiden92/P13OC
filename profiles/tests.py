from django.test import TestCase
from django.test import Client

from .models import Profile, User


class TestProfile(TestCase):
    """A class to represent a test profile

    Arguments:
        TestCase -- object: TestCase
    """
    def setUp(self) -> None:
        """Method to set up the test configuration
        """
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
            favorite_city=self.favorite_city)

    def test_profile(self) -> None:
        """Method to test profile
        """
        self.assertEqual(self.profile.user, self.user)

    def test_profile_favorite_city(self) -> None:
        """Method to test profile favorite city
        """
        self.favorite_city = "Madrid"
        self.assertNotEqual(self.profile.favorite_city, self.favorite_city)


# Test index view
class TestIndexView(TestCase):
    """A class to represent a test index view
        Arguments:
            TestCase -- object: TestCase
    """
    def setUp(self) -> None:
        """Method to set up the test configuration
        """
        self.client = Client()
        self.profiles_list = Profile.objects.all()
        self.response = self.client.get('/')

    def test_response(self) -> None:
        """Method to test response
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self) -> None:
        """Method to test template
        """
        self.assertTemplateUsed(self.response, 'index.html')


# Test index view
class TestProfileView(TestCase):
    """A class to represent a test profile view

    Arguments:
        TestCase -- object: TestCase
    """
    def setUp(self) -> None:
        """Method to set up the test configuration
        """
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
            favorite_city="Rueil")
        self.client = Client()
        self.response = self.client.get(f'/profiles/{self.user.username}/')

    def test_response(self) -> None:
        """Method to test response
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self) -> None:
        """Method to test template
        """
        self.assertTemplateUsed(self.response, 'profiles/profile.html')


# Test index view
class TestProfilesView(TestCase):
    """A class to represent a test profiles view

    Arguments:
        TestCase -- object: TestCase
    """
    def setUp(self) -> None:
        """Method to set up the test configuration
        """
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
            favorite_city="Rueil")
        self.client = Client()
        self.response = self.client.get(f'/profiles/')

    def test_response(self) -> None:
        """Method to test response
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self) -> None:
        """Method to test template
        """
        self.assertTemplateUsed(self.response, 'profiles/index.html')
