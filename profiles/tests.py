from django.test import TestCase, Client
from django.urls import reverse


from .models import Profile, User
from profiles.apps import ProfilesConfig


class TestProfile(TestCase):
    """Class for testing the Profile model."""
    def setUp(self):
        """Initialization of data for tests."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_create_profile(self):
        """Method to test a profile creation."""
        profile = Profile.objects.create(user=self.user, favorite_city='Test City')

        # Assert that the profile is created successfully
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.favorite_city, 'Test City')

    def test_read_profile(self):
        """Method to test a profile read."""
        profile = Profile.objects.create(user=self.user, favorite_city='Test City')

        # Retrieve the profile from the database
        retrieved_profile = Profile.objects.get(user=self.user)

        # Assert that the retrieved profile matches the created profile
        self.assertEqual(retrieved_profile, profile)

    def test_update_profile(self):
        """Method to test a profile update."""
        profile = Profile.objects.create(user=self.user, favorite_city='Test City')

        new_favorite_city = 'New City'
        profile.favorite_city = new_favorite_city
        profile.save()

        updated_profile = Profile.objects.get(user=self.user)

        self.assertEqual(updated_profile.favorite_city, new_favorite_city)

    def test_delete_profile(self):
        """Method to test a profile delete."""
        profile = Profile.objects.create(user=self.user, favorite_city='Test City')
        profile.delete()

        self.assertEqual(Profile.objects.count(), 0)


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
