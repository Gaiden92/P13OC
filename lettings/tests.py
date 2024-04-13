from django.test import TestCase, Client

from .models import Letting, Address


class TestLetting(TestCase):
    def setUp(self) -> None:

        self.address = Address.objects.create(
            number=9,
            street="allée des citronniers",
            city="Suresnes",
            state="92",
            zip_code=92150,
            country_iso_code="FRA")
        
        self.letting = Letting.objects.create(title="title letting", address=self.address)
         
    def test_letting(self):
        self.assertEqual(self.letting.address, self.address)

    def test_letting_title(self):
        self.title= "Other title"
        self.assertNotEqual(self.letting.title, self.title)
    
    def test_letting_address(self):
        self.address= Address.objects.create(
            number=10,
            street="allée des Bananiers",
            city="Rueil",
            state="92",
            zip_code=92150,
            country_iso_code="FRA")
        
        self.assertNotEqual(self.letting.address, self.address)


# Test index view
class TestIndexView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get('/lettings/')

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'lettings/index.html')


class TestLettingsView(TestCase):
    def setUp(self) -> None:

        self.address = Address.objects.create(
            number=9,
            street="allée des citronniers",
            city="Suresnes",
            state="92",
            zip_code=92150,
            country_iso_code="FRA")
        
        self.letting = Letting.objects.create(title="title letting", address=self.address)

        self.client = Client()
        self.response = self.client.get('/lettings/')

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'lettings/index.html')


class TestLettingsView(TestCase):
    def setUp(self) -> None:

        self.address = Address.objects.create(
            number=9,
            street="allée des citronniers",
            city="Suresnes",
            state="92",
            zip_code=92150,
            country_iso_code="FRA")
        
        self.letting = Letting.objects.create(title="title letting", address=self.address)

        self.client = Client()
        self.response = self.client.get(f'/lettings/{self.letting.id}/')

    def test_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'lettings/letting.html')