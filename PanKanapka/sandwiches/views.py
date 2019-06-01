from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from orders.models import Order, OrderSandwiches
from .models import Sandwich, Ingredient



def sandwiches(request):
    object_list = Sandwich.objects.all()
    current_order_products = []

    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(user=request.user, is_ordered=False)

        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.sandwiches.all()
            current_order_products = [product.sandwich for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }
    return render(request, "sandwiches_list.html", context)


@login_required()
def create_sandwich(request):
    object_list = Ingredient.objects.all()
    context = {
        'object_list': object_list,
    }

    return render(request, "new_sandwich.html", context)


@login_required()
def new_sandwich(request):
    ingredients = request.POST.getlist('ingredient')
    object_list = Ingredient.objects.filter(id__in=ingredients)
    context = {
        'object_list': object_list,
    }
    return render(request, "composed_sandwich.html", context)


@login_required()
def confirm_new_sandwich(request):
    ingredients = request.POST.getlist('ingredient')
    object_list = Ingredient.objects.filter(id__in=ingredients)
    sandwich = Sandwich()
    sandwich.name = "Kanapka oryginalna"
    sandwich.price = sum([ingredient.price for ingredient in object_list])
    sandwich.accessible = False
    sandwich.image = "/sandwiches/images/s1.jpg"
    sandwich.save()

    for ingredient in object_list:
        sandwich.ingredients.add(ingredient)

    order_item, status = OrderSandwiches.objects.get_or_create(sandwich=sandwich, user=request.user)
    user_order, status = Order.objects.get_or_create(user=request.user, is_ordered=False)
    user_order.sandwiches.add(order_item)
    if status:
        user_order.save()
    return redirect(reverse('orders:summary'))
