from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.urls import reverse


from clients.models import Uzytkownik
from bulka.models import Kanapki
from orders.models import OrderSandwiches, Order


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Uzytkownik, email=request.user)
    order = Order.objects.filter(super_user=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def make_single_order(request, **kwargs):
    user_profile = get_object_or_404(Uzytkownik, email=request.user)
    sandwich = Kanapki.objects.filter(id=kwargs.get('kanapka', "")).first()
    order_item, status = OrderSandwiches.objects.get_or_create(sandwich=sandwich)
    user_order, status = Order.objects.get_or_create(super_user=user_profile, is_ordered=False)
    user_order.sandwiches.add(order_item)
    if status:
        user_order.save()

    messages.info(request, "zamówienie złożone")
    return redirect(reverse('sandwiches:sandwiches'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'summary.html', context)
