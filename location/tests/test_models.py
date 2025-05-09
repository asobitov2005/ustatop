from django.test import TestCase
from location.models import City, Address, CustomUser



class LocationModelTest(TestCase):
    def test_create_city(self):
        city = City.objects.create(
            name="Tashkent",
        )
        self.assertEqual(city.name, "Tashkent")



    def test_create_address(self):
        self.user = CustomUser.objects.create_user(first_name='Alisa',email="test@example.com")
        self.city = City.objects.create(name="Tashkent")


        address = Address.objects.create(
            name="Falonchi address",
            booking_address=self.user,
            city=self.city
        )
        self.assertEqual(address.name, "Falonchi address")
        self.assertEqual(address.booking_address, self.user)
        self.assertEqual(address.city, self.city)