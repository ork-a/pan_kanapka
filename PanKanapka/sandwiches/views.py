from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import Order, OrderSandwiches
from .models import Sandwich, IngredientGroup, Ingredient
from django.shortcuts import redirect
from django.urls import reverse


def sandwiches(request):
    sandwiches_list = [{'sandwich': sandwich} for sandwich in Sandwich.objects.all()]

    for sandwich_dict in sandwiches_list:
        allergens = []
        for ingredient in sandwich_dict['sandwich'].ingredients.all():
            for allergen in ingredient.allergen.all():
                allergens.append(allergen)
        sandwich_dict.update({'allergens': set(allergens)})

    current_order_products = []

    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(user=request.user, is_ordered=False)

        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.sandwiches.all()
            current_order_products = [product.sandwich for product in user_order_items]

    context = {
        'object_list': sandwiches_list,
        'current_order_products': current_order_products
    }

    return render(request, "sandwiches_list.html", context)


def single_sandwich(request, sandwich_id):
    sandwich = Sandwich.objects.get(pk=sandwich_id)

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
