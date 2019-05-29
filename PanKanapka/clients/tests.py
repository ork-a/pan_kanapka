from django.test import TestCase, Client
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.utils import IntegrityError
from .models import User
from .forms import RegisterForm
from .views import add_new_user
from unittest import skip

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


    def test_correct_registration(self):
        data = {'email': 'test8901@wp.pl',
                'name': 'jacek',
                'surname': 'tomczak',
                'password1': 'test1',
                'password2': 'test1'}
        form = RegisterForm(data= data)
        self.assertTrue(form.is_valid(),form.errors)

    def test_form_for_incorrect_email(self):
        data = {'email': 'jacek'}
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        with self.assertRaises(ValueError):
            form.save(commit=False)

    def test_duplicate_email(self):
        data = {'email': 'jacek@wp.pl',
                'name': 'jacek',
                'surname': 'tomczak',
                'password1': 'test2',
                'password2': 'test2'}
        User.objects.create_user(email=data['email'],password=data['password1'])
        with self.assertRaises(ValueError):
            form = RegisterForm(data=data)
            form.save(commit=False)

    def test_two_different_password(self):
        data = {'email': 'jacek888@wp.pl',
                'name': 'jacek',
                'surname': 'tomczak',
                'password1': 'abdul',
                'password2': 'test33'}
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Hasła nie są identyczne'])

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

    @skip
    def test_two_different_password(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['email'] = 'jacek@ppp.pl'
        request.POST['password1'] = 'admin'
        request.POST['password2'] = 'admin2'
        response = add_new_user(request)
        self.assertIn(b'class="errorlist"', response.content)
        self.assertIn(b'identyczne', response.content)
