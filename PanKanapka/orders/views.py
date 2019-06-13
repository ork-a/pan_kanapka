import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from clients.models import User
from orders.models import OrderSandwiches, Order, OrderStatus
from sandwiches.models import Sandwich


def get_user_pending_order(request):
    user_profile = get_object_or_404(User, email=request.user)
    try:
        order = Order.objects.get(user=user_profile, status__status="W koszyku")
    except ObjectDoesNotExist:
        order = None
    if request.POST:
        order.remarks = request.POST['order_remarks']
        order.save()
    return order


def get_user_ordered_items(request):
    user_profile = get_object_or_404(User, email=request.user)
    try:
        order = Order.objects.filter(user=user_profile, status__status="Potwierdzone")
    except ObjectDoesNotExist:
        order = None
    return order


def get_summary_company_order(request):
    user_company = get_object_or_404(User, email=request.user).group
    orders = Order.objects.filter(user__group=user_company, is_ordered=False)
    if orders.exists():
        return orders
    return


@login_required()
def make_single_order(request, **kwargs):
    sandwich = Sandwich.objects.get(id=kwargs.get('kanapka', ""))
    in_basket_status = OrderStatus.objects.get(status="W koszyku")
    order, created = Order.objects.get_or_create(user=request.user, status=in_basket_status)

    order_item, created = OrderSandwiches.objects.get_or_create(sandwich=sandwich, order=order)
    if not created:
        order_item.quantity += 1
        order_item.save()

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
    pending_order = get_user_pending_order(request)
    sandwiches_in_basket = OrderSandwiches.objects.filter(order=pending_order)
    order_price = sum([item.sandwich.price * item.quantity for item in sandwiches_in_basket])
    context = {
        'sandwiches_in_basket': sandwiches_in_basket,
        'order_price': order_price,
    }
    return render(request, 'summary_user.html', context)


@login_required()
def confirm_order(request):
    pending_order = get_user_pending_order(request)
    pending_order.status = OrderStatus.objects.get(status="Potwierdzone")
    pending_order.date_ordered = datetime.datetime.strptime(request.POST['order_date'], "%d-%m-%Y")
    pending_order.remarks = request.POST['order_remarks']
    pending_order.save()

    messages.info(request, "Zamówienie zostało złożone. Możesz je podejrzeć w Zamówieniach.")
    return redirect(reverse('orders:show_confirmed_order'))


@login_required()
def show_confirmed_order(request):
    confirmed_orders = get_user_ordered_items(request)
    order_sandwiches = {order.pk: (
        order,
        sum([item.sandwich.price * item.quantity for item in OrderSandwiches.objects.filter(order=order)]),
        OrderSandwiches.objects.filter(order=order)
    ) for order in confirmed_orders}
    context = {
        'confirmed_orders': order_sandwiches,
    }
    return render(request, 'placed_orders.html', context)
