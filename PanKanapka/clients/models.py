from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Organizacja(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    adres = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa


class ClientManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Użytkownik musi posiadać adres email.')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.obsluga = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.obsluga = True
        user.admin = True
        user.save(using=self._db)
        return user


class Uzytkownik(AbstractBaseUser):
    email = models.CharField(max_length=100, default=None, unique=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    aktywny = models.BooleanField(default=True)
    grupa = models.ForeignKey(Organizacja, on_delete=models.SET_NULL, null=True, blank=True)
    obsluga = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.obsluga

    @property
    def is_active(self):
        return self.aktywny

    objects = ClientManager()
