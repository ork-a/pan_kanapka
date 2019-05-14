import datetime

from django.db import models

from bulka.models import Kanapki
from clients.models import Uzytkownik


class OrderSandwiches(models.Model):
    sandwich = models.ForeignKey(Kanapki, on_delete=models.DO_NOTHING)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.sandwich.Kan_Nazwa


class Order(models.Model):
    super_user = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, null=True)  # super_user should be changed to user
    is_ordered = models.BooleanField(default=False)
    sandwiches = models.ManyToManyField(OrderSandwiches)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_order(self):
        return self.sandwiches.all()

    def get_total(self):
        return sum([sandwich.sandwich.Kan_Cena for sandwich in self.sandwiches.all()])

    def __str__(self):
        return '{} - {}'.format(self.super_user.grupa.nazwa, datetime.date.today().strftime('%d-%m-%Y'))
