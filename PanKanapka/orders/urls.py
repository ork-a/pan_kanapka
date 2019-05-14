from django.conf.urls import url

from .views import make_single_order, order_details, delete_sandwich

app_name = 'orders'

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^zamow-kanapke/(?P<kanapka>[-\w]+)/$', make_single_order, name="single_order"),
    url(r'^summary/$', order_details, name="summary"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_sandwich, name='delete_sandwich'),
]