from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, UserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password, role='user'):
        if not email:
            raise ValueError('Users emaili bo\'shi lo\'zim')
        if not first_name:
            raise ValueError("Userni ismi bo'lisji lo'zim")
        if not last_name:
            raise ValueError("Userni familiyasi bo'lishi lo'zim")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role='admin'
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractUser, PermissionsMixin):
    ROLE_SYSTEM = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=55, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    number = models.BigIntegerField(default=0)
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_SYSTEM, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
