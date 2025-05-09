from django.test import TestCase
from user.models import CustomUser


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            first_name="Ali",
            last_name="Valiyev",
            email="ali@example.com",
            password="testpass123"
        )

        self.assertEqual(user.first_name, "Ali")
        self.assertEqual(user.last_name, "Valiyev")
        self.assertEqual(user.email, "ali@example.com")
        self.assertTrue(user.check_password("testpass123"))
        self.assertEqual(user.role, "client")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin = CustomUser.objects.create_superuser(
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            password="adminpass123"
        )

        self.assertEqual(admin.first_name, "Admin")
        self.assertEqual(admin.last_name, "User")
        self.assertEqual(admin.email, "admin@example.com")
        self.assertTrue(admin.check_password("adminpass123"))
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertEqual(admin.role, "client")


    def test_no_email(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                first_name="NoEmail",
                last_name="User",
                email="",
                password="somepass"
        )

    def test_admin_staff_false(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email="admin2@example.com",
                password="adminpass123",
                is_staff=False,
                is_superuser=True
            )

    def test_user_str_method(self):
        user = CustomUser.objects.create_user(
            first_name="Ali",
            last_name="Valiyev",
            email="ali@example.com",
            password="testpass123"
        )
        self.assertEqual(str(user), "Ali, Valiyev")
