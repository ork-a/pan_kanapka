from django.test import TestCase
from django.http import HttpRequest

from .models import Sandwich
from .views import sandwiches, plus_minus_view
from orders.models import OrderSandwiches, Order
from clients.models import User

import unittest.mock as mock
from unittest.mock import MagicMock, PropertyMock
from unittest import skip

class TestPlusMinusButton(TestCase):

    def setUp(self):
        # create sandwich
        sandwich1 = Sandwich(name='z lisaciami debu', price=5)
        sandwich1.save()
        sandwich2 = Sandwich(name='z jablkiem', price=3)
        sandwich2.save()
        sandwich3 = Sandwich(name='szynka, bez jaj', price=13)
        sandwich3.save()

    def test_created_sandwiches(self):
        object_list = Sandwich.objects.all()
        self.assertEqual(object_list.count(), 3)

    def test_simple_order(self):
        sandwich = Sandwich.objects.get(id=1)
        order = OrderSandwiches(sandwich=sandwich, quantity=2)
        order.save()
        order_list = Order()
        order_list.save()
        order_list.sandwiches.add(order)
        self.assertIn(order, order_list.sandwiches.all())

    def test_not_authenticate_user(self):
        mock = MagicMock()
        type(mock).is_authenticated = PropertyMock(return_value=False)

        request = HttpRequest()
        request.method = 'POST'
        request.user = mock
        request.POST['id'] = 1

        response = plus_minus_view(request)
        self.assertEqual('uzytkownik nie zalogowany', response)

    def test_same_sandwich_order_multi_time_by_POST_request(self):
        mock = MagicMock()
        type(mock).is_authenticated = PropertyMock(return_value=True)

        request = HttpRequest()
        request.method = 'POST'
        request.user = mock
        request.POST['id'] = 1
        request.POST['quantity'] = 1

        #first order
        sandwich = Sandwich.objects.get(id = 1)
        correct_sandwich = OrderSandwiches(sandwich=sandwich, quantity=1)
        correct_quantity = 1
        order_view = plus_minus_view(request)
        self.assertEqual(correct_quantity, order_view.quantity)
        self.assertEqual(correct_sandwich.sandwich, order_view.sandwich)

        quantity_value = [1,0,-3,15,2,10,30,]
        for value in quantity_value:
            request.POST['quantity'] = value
            correct_quantity = 1 + value
            with self.subTest():
                order_view = plus_minus_view(request)
                self.assertEqual(correct_quantity, order_view.quantity)