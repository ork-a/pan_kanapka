from selenium import webdriver
from django.test import LiveServerTestCase

class RegistrationTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_get__registration_site(self):
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.close()