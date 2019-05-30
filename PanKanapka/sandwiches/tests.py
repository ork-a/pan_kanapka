from django.test import TestCase

from .models import Sandwich
from orders.models import OrderSandwiches, Order
# Create your tests here.
class TestPlusMinusButton(TestCase):

    def setUp(self):
        # create sandwich
        sandwich1 = Sandwich(name='z lisaciami debu', price=5)
        sandwich1.save()
        sandwich2 = Sandwich(name='z jablkiem', price=3)
        sandwich2.save()
        sandwich3 = Sandwich(name='Szynka, bez jaj', price=13)
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
