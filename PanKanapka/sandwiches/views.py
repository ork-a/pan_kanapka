from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import OrderSandwiches, Order, OrderStatus
from .models import Sandwich, IngredientGroup, Ingredient
from django.shortcuts import redirect
from django.urls import reverse


def sandwiches(request):
    sandwiches_list = Sandwich.objects.all()
    context = {
        'object_list': sandwiches_list,
    }
    return render(request, "sandwiches_list.html", context)


def single_sandwich(request, sandwich_id):
    sandwich = Sandwich.objects.get(pk=sandwich_id)
    sandwich.get_allergens()
    context = {
        'sandwich': sandwich,
    }
    return render(request, "single_sandwich.html", context)


@login_required()
def create_sandwich(request):
    sorted_ingredients = {}
    ingredient_groups = IngredientGroup.objects.all()
    for ingredient_group in ingredient_groups:
        ingredients_of_group = Ingredient.objects.filter(group=ingredient_group)
        sorted_ingredients.update({ingredient_group.name: ingredients_of_group})
    context = {
        'object_list': sorted_ingredients,
    }

    return render(request, "new_sandwich.html", context)


@login_required()
def new_sandwich(request):
    ingredients = request.POST.getlist('ingredient')
    object_list = Ingredient.objects.filter(id__in=ingredients)
    total_price = sum([ingredient.price for ingredient in object_list])
    context = {
        'object_list': object_list,
        'total_price': total_price
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
    sandwich.save()

    for ingredient in object_list:
        sandwich.ingredients.add(ingredient)

    in_basket_status = OrderStatus.objects.get(status="W koszyku")
    order, created = Order.objects.get_or_create(user=request.user, status=in_basket_status)

    OrderSandwiches.objects.get_or_create(sandwich=sandwich, order=order)

    return redirect(reverse('orders:summary'))


def plus_minus_view(request):
    if request.method == 'POST':
        sandwich = Sandwich.objects.get(id=request.POST['id'])
        order_sandwich = OrderSandwiches.objects.filter(sandwich=sandwich)
        if not order_sandwich.exists():
            new_order = OrderSandwiches(sandwich=sandwich, quantity=1)
            new_order.save()
            return new_order
        else:
            next_order = OrderSandwiches.objects.get(sandwich=sandwich)
            next_order.quantity += 1
            return next_order
