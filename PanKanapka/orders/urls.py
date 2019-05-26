from django.urls import path

from .views import make_single_order, order_details, delete_sandwich, update_quantity, summary_order, confirm_order

app_name = 'orders'

urlpatterns = [  # pylint: disable=invalid-name
    path('zamow-kanapke/<int:kanapka>/', make_single_order, name="single_order"),
    path('zamowienie/', order_details, name="summary"),
    path('kanapka/usun/<int:item_id>/', delete_sandwich, name='delete_sandwich'),
    path('kanapka/aktualizuj_ilosc/<int:item_id>/<int:quantity>/', update_quantity, name='update_quantity'),
    path('zamowienie-zbiorcze/', summary_order, name='summary_order'),
    path('potwierdz-zamowienie/', confirm_order, name='confirm_order'),
]
