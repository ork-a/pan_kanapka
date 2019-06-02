from django.test import TestCase
from django.http.request import HttpRequest

from .views import sandwiches

# Create your tests here.
class ListSandwichTest(TestCase):
    def setUp(self):
        pass

    def test_sandiwch_view(self):
        request = HttpRequest()
        request.method = 'GET'

        response = sandwiches(request)
        self.assertTemplateUsed(response, "sandwiches_list.html")