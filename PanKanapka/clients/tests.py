from django.test import TestCase
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from .models import User
from .views import registration_form

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

    def test_website_handle_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name'] = 'name'
        response = registration_form(request)

    def test_website_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['email'] = 'ppp@pp.pl'
        request.POST['name'] = 'ppp'
        response = registration_form(request)
        self.assertEqual(User.objects.all().count(), 1)


class ListAndModelTest(TestCase):
    def test_cannot_save_empty_record(self):
        user = User.objects.create(email='jacek')
        with self.assertRaises(ValidationError):
            user.save()
            user.full_clean()