from django.test import TestCase

from .models import Sandwich
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

    def test_first(self):
        object_list = Sandwich.objects.all()
        for sandwich in object_list:
            print(sandwich.id, sandwich.name)