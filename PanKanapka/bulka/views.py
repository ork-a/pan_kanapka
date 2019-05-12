from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import Order
from .models import Kanapki


@login_required
def sandwiches(request):
    object_list = Kanapki.objects.all()
    filtered_orders = Order.objects.filter(super_user=request.user, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.sandwiches.all()
        current_order_products = [product.sandwich for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "sandwiches_list.html", context)
