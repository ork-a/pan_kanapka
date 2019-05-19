from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.urls import reverse


from clients.models import User
from sandwiches.models import Sandwich
from orders.models import OrderSandwiches, Order


def get_user_pending_order(request):
    user_profile = get_object_or_404(User, email=request.user)
    order = Order.objects.filter(user=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


def get_summary_company_order(request):
    user_company = get_object_or_404(User, email=request.user).group
    orders = Order.objects.filter(user__group=user_company, is_ordered=False)
    if orders.exists():
        return orders
    return


@login_required()
def make_single_order(request, **kwargs):
    user_profile = get_object_or_404(User, email=request.user)
    sandwich = Sandwich.objects.filter(id=kwargs.get('kanapka', "")).first()
    order_item, status = OrderSandwiches.objects.get_or_create(sandwich=sandwich, user=request.user)
    user_order, status = Order.objects.get_or_create(user=user_profile, is_ordered=False)
    user_order.sandwiches.add(order_item)
    if status:
        user_order.save()

    messages.info(request, "zamówienie złożone")
    return redirect(reverse('orders:summary'))


@login_required()
def delete_sandwich(request, item_id):
    item_to_delete = OrderSandwiches.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Kanapka usunięta")
    return redirect(reverse('orders:summary'))


@login_required()
def update_quantity(request, item_id, quantity):
    OrderSandwiches.objects.filter(pk=item_id).update(quantity=quantity)
    messages.info(request, "Ilość zaktualizowana")
    return redirect(reverse('orders:summary'))


@login_required()
def order_details(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'summary_user.html', context)


@login_required()
def summary_order(request):
    existing_orders = get_summary_company_order(request)
    context = {
        'company_orders': existing_orders
    }
    return render(request, 'summary_company.html', context)
