from django.test import TestCase
from django.http import HttpRequest

from .models import Sandwich
from .views import sandwiches, plus_minus_view
from orders.models import OrderSandwiches, Order
from clients.models import User

import unittest.mock as mock
from unittest.mock import MagicMock, PropertyMock


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

    def test_add_sandwich_by_POST_request(self):
        mock = MagicMock()
        type(mock).is_authenticated = PropertyMock(return_value=True)

        request = HttpRequest()
        request.method = 'POST'
        request.user = mock
        request.POST['id'] = 1

        sandwich = Sandwich.objects.get(id = 1)
        order_correct = OrderSandwiches(sandwich=sandwich, quantity=1)
        order_viw = plus_minus_view(request)
        self.assertEqual(order_correct.quantity, order_viw.quantity)
        self.assertEqual(order_correct.sandwich, order_viw.sandwich)

