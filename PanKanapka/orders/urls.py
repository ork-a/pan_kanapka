from django.conf.urls import url

from .views import make_single_order, order_details

app_name = 'orders'

urlpatterns = [
    url(r'^zamow-kanapke/(?P<kanapka>[-\w]+)/$', make_single_order, name="single_order"),
    url(r'^summary/$', order_details, name="summary")
]