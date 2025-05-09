from django.test import TestCase
from service.models import Service, Booking, Rating, CustomUser

class ServiceModelTest(TestCase):
    def test_create_service(self):
        self.user = CustomUser.objects.create_user(first_name='Alisa', email="test@example.com")
        self.service = Service.objects.create(service_type="cleaning", price="50", provider=self.user)

        service = Service.objects.create(
            service_type="cleaning",
            description="Bir nimalar",
            provider=self.user,
            price=50
        )

        self.assertEqual(service.service_type, "cleaning")
        self.assertEqual(service.description, "Bir nimalar")
        self.assertEqual(service.provider, self.user)
        self.assertEqual(service.price, 50)

    def test_create_booking(self):
        self.user = CustomUser.objects.create_user(first_name='Alisa', email="test@example.com")
        self.service = Service.objects.create(service_type="cleaning", price="50", provider=self.user)

        booking = Booking.objects.create(
            client=self.user,
            service=self.service,
            status="kutish",
            date="2025-05-18"
        )

        self.assertEqual(booking.client, self.user)
        self.assertEqual(booking.service, self.service)
        self.assertEqual(booking.status, 'kutish')
        self.assertEqual(booking.date, "2025-05-18")

    def test_create_rating(self):
        self.user = CustomUser.objects.create_user(first_name='Alisa', email="test@example.com")
        self.service = Service.objects.create(service_type="cleaning", price="50", provider=self.user)
        self.booking = Booking.objects.create(client=self.user, service=self.service, status="kutish",date="2025-05-18")

        rating = Rating.objects.create(
            user=self.user,
            booking=self.booking,
            rating=4,
            comment="hello"
        )

        self.assertEqual(rating.user, self.user)
        self.assertEqual(rating.booking, self.booking)
        self.assertEqual(rating.rating, 4)
        self.assertEqual(rating.comment, "hello")
