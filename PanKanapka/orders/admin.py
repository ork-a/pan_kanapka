from django.contrib import admin
from .models import Order, OrderSandwiches
from django.urls import path
from django.shortcuts import render, redirect
from django.urls import reverse
from clients.models import User, Company


class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_company')
    list_filter = ('user__group__name',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin_orders', self.admin_orders)
        ]
        return custom_urls + urls

    def admin_orders(self, request):

        ingredients = {}
        html = ''
        for company in Company.objects.all():
            if OrderSandwiches.objects.filter(order__user__group=company):
                html += '<div class="company"><h4>{}</h4>'.format(company.name)
                for user in User.objects.filter(group=company):
                    if OrderSandwiches.objects.filter(order__user=user):
                        html += '<div class="user"><span class="user_name">{} {}</span><hr>'.format(user.surname, user.name)
                        for order in Order.objects.filter(status__status="Potwierdzone", user=user):
                            html += '<div class="order"><p><strong>{}</strong> - <span class="remarks">{}</span></p>'.format(order.date_ordered, order.remarks)
                            for item in OrderSandwiches.objects.filter(order=order):
                                html += '<div class="sandwich"><p><span class="quantity">{}</span> x <span class="sandwich">{}</span> [{}]</p>'.format(
                                    item.quantity, item.sandwich.name, ', '.join(([x.name for x in item.sandwich.ingredients.all()])))
                                for ingredient in item.sandwich.ingredients.all():
                                    if ingredient.name not in ingredients:
                                        ingredients[ingredient.name] = 1
                                    else:
                                        ingredients[ingredient.name] += 1
                                html += '</div>'
                            html += '</div><hr>'
                        if OrderSandwiches.objects.filter(order__user=user):
                            html += '</div>'
                if OrderSandwiches.objects.filter(order__user__group=company):
                    html += '</div>'

        context = {
            'orders': html,
            'ingredients': ingredients
        }

        if request.user.staff:
            return render(request, 'admin_orders.html', context)
        else:
            return redirect(reverse('sandwiches:sandwiches'))


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderSandwiches)
