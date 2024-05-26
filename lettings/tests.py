from django.test import TestCase, Client
from django.urls import reverse
from django.apps import apps

from .models import Letting, Address
from lettings.apps import LettingsConfig


class TestLetting(TestCase):
    """A class to represent tests for Letting model"""

    def setUp(self) -> None:
        """Method to set up the test configuration"""
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code="12345",
            country_iso_code="TST",
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_letting(self) -> None:
        """Method to test letting"""
        self.assertEqual(self.letting.title, "Test Letting")
        self.assertEqual(self.letting.address, self.address)


class TestLettingsIndexView(TestCase):
    """A class to represent tests for the lettings index view"""

    def setUp(self) -> None:
        """Method to set up the test configuration"""
        self.client = Client()
        self.response = self.client.get(reverse('lettings_index'))

    def test_response(self) -> None:
        """Method to test response"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self) -> None:
        """Method to test template"""
        self.assertTemplateUsed(self.response, 'lettings/index.html')


class TestLettingView(TestCase):
    """A class to represent tests for the letting view"""

    def setUp(self) -> None:
        """Method to set up the test configuration"""
        self.client = Client()
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code="12345",
            country_iso_code="TST",
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_letting_view(self) -> None:
        """Method to test letting view"""
        response = self.client.get(reverse('letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.letting.address.street)

    def test_letting_view_nonexistent_letting(self) -> None:
        """Method to test letting view with a nonexistent letting"""
        response = self.client.get(reverse('letting', args=[999]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lettings_index'))


class LettingsConfigTest(TestCase):
    """A class to represent tests for LettingsConfig"""

    def test_app_config(self):
        """Method to test the lettings app configuration"""
        self.assertEqual(LettingsConfig.name, 'lettings')
        self.assertEqual(apps.get_app_config('lettings').name, 'lettings')
