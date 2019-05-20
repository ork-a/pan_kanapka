from django.test import TestCase
from .models import User

# Create your tests here.

class CreateUserTest(TestCase):

    def test_saving_and_retriving_new_user(self):
        first_user = User()
        first_user.email = 'ppp1@pl.pl'
        first_user.name = 'pierwszy_name'
        first_user.surname = 'pierwszy_surname'
        first_user.active = False
        first_user.save()

        second_user = User()
        second_user.email = 'ppp2@pl.pl'
        second_user.name = 'second_name'
        second_user.surname = 'second_surname'
        second_user.active = False
        second_user.save()

        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 2)