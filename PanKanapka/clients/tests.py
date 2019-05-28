from django.test import TestCase, Client
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.utils import IntegrityError
from .models import User
from .forms import RegisterForm

# Create your tests here.

class RegisterFormTest(TestCase):

    def test_form_render_text_input(self):
        form = RegisterForm()
        self.assertIn('wpisz adres email', form.as_p())

    def test_form_for_blank_email(self):
        form =  RegisterForm(data={'email':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'],
            ['Pole adres email nie może być puste']
        )

    def test_empty_form_has_no_error(self):
        form = RegisterForm()
        empty_dict = {}
        self.assertEqual(form.errors, empty_dict)

    # def test_form_for_incorrect_email(self):
    #     data = {'email': 'jacek'}
    #     # with self.assertRaises(ValidationError):
    #     form = RegisterForm(data=data)
    #     form.full_clean()
    #     self.assertFalse(form.is_valid())

    def test_duplicate_email(self):
        data = {'email': 'jacek888@wp.pl',
                'name': 'jacek',
                'surname': 'tomczak',
                'password': 'admin',
                'password2': 'admin'}
        form = RegisterForm(data=data)
        print (form.is_valid())
        print(form.full_clean())

    def test_two_different_password(self):
        data = {'email': 'jacek888@wp.pl',
                'name': 'jacek',
                'surname': 'tomczak',
                'password': 'admin',
                'password2': 'admin2'}
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

class RegistrationViewTest(TestCase):
    client = Client()
    def test_if_used_registration_form(self):
        response = self.client.get('/clients/add')
        self.assertIsInstance(response.context['form'], RegisterForm)

    def test_if_used_registration_template(self):
        response = self.client.get('/clients/add')
        self.assertTemplateUsed(response, 'add_new_user.html')

    def test_empty_form_has_no_error(self):
        response = self.client.get('/clients/add')
        self.assertNotIn(b'class="errorlist"', response.content)