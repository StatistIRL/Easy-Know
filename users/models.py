from django.db import models
from django.contrib.auth.models import UserManager as DjangoUserManager, AbstractUser
import uuid

# Create your models here.


class CustomUserManager(DjangoUserManager):
    def _create_user(self, username, email, password, **extra_fields):  # -> Any:
        if username is None:
            raise ValueError("Имя пользователя обязательное поле.")
        if email is None:
            raise ValueError("Почта обязательное поле.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        user = self._create_user(
            username=username, email=email, password=password, **extra_fields
        )
        return user

    def create_superuser(
        self, username, email, password=None, **extra_fields
    ):  # -> Any:
        user = self._create_user(
            username=username, email=email, password=password, **extra_fields
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(db_index=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
