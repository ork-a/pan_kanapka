import datetime

from django.db import models

from sandwiches.models import Sandwich
from clients.models import User


class OrderSandwiches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sandwich = models.ForeignKey(Sandwich, on_delete=models.DO_NOTHING)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '{} - {}'.format(self.user.name, self.sandwich.name)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # possibly get rid of this - data duplication
    is_ordered = models.BooleanField(default=False)
    sandwiches = models.ManyToManyField(OrderSandwiches)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_order(self):
        return self.sandwiches.all()

    def get_company(self):
        return self.user.group.name

    def get_username(self):
        return '{} {}'.format(self.user.name, self.user.surname)

    def get_sandwiches(self):
        return ', '.join([sandwich.sandwich.name for sandwich in self.sandwiches.all()])

    def get_total(self):
        return sum([sandwich.sandwich.price * sandwich.quantity for sandwich in self.sandwiches.all() if not sandwich.is_ordered])

    def __str__(self):
        return '{} - {} - {}'.format(self.user.group.name,
                                     self.user.name,
                                     datetime.date.today().strftime('%d-%m-%Y'))
