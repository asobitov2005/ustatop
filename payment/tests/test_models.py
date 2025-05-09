from django.test import TestCase
from payment.models import Payment
from user.models import CustomUser
from service.models import Service


class PaymentModelTest(TestCase):
    def test_create_payment(self):
        self.user = CustomUser.objects.create_user(first_name='Alisa', email="test@example.com")
        self.service = Service.objects.create(service_type="cleaning", price="50", provider=self.user)

        payment = Payment.objects.create(
            user=self.user,
            service=self.service,
            status="pending",
            payment_method="cash",
            amount=40,
            date="2025-05-12"
        )

        self.assertEqual(payment.user, self.user)
        self.assertEqual(payment.service, self.service)
        self.assertEqual(payment.status, "pending")
        self.assertEqual(payment.payment_method, "cash")
        self.assertEqual(payment.amount, 40)

