from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        return self._create_user(email, username, password, is_superuser=False)

    def create_superuser(self, email, username, password=None):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    # para asignar el manager :)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users_key', default=2) # santiagorhenals1@gmail.com by default
    name = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name