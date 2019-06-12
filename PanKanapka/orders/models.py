import datetime

from django.db import models

from sandwiches.models import Sandwich
from clients.models import User


class OrderStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_ordered = models.DateField(auto_now=False, auto_now_add=False, null=True)
    remarks = models.TextField(max_length=300, blank=True, null=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Zamówienie'
        verbose_name_plural = 'Zamówienia'

    def get_company(self):
        return self.user.group.name

    def get_username(self):
        return '{} {}'.format(self.user.name, self.user.surname)

    def __str__(self):
        return '{} - {}'.format(self.user.group.name,
                                     self.user.name)


class OrderSandwiches(models.Model):
    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Kanapka w zamówieniu'
        verbose_name_plural = 'Kanapki w zamówieniach'

    def __str__(self):
        return '{}'.format(self.sandwich.name)
