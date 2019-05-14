from django.conf.urls import url
from django.urls import path

from .views import make_single_order, order_details, delete_sandwich, update_quantity

app_name = 'orders'

urlpatterns = [  # pylint: disable=invalid-name
    path('zamow-kanapke/<int:kanapka>/', make_single_order, name="single_order"),
    path('summary/', order_details, name="summary"),
    path('item/delete/<int:item_id>/', delete_sandwich, name='delete_sandwich'),
    path('item/update_quantity/<int:item_id>/<int:quantity>/', update_quantity, name='update_quantity'),
]
