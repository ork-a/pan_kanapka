from selenium import webdriver
from django.test import LiveServerTestCase

from time import sleep


class RegistrationTest(LiveServerTestCase):
    #Użytkownik otwiera przeglarkę
    def setUp(self):
        self.browser = webdriver.Firefox()
    # Użytkownik wchodzi na stronę główną
    def test_get_registration_site(self):
        self.browser.get(self.live_server_url)
        # Użytkownik klika zaloguj
        sleep(20)
        self.browser.find_elements

    # Użytkownik jest przeniesiony na stronę logowania
    # Użytkownik wpisuje dane do logowania (email, hasło) i klika zaloguj
    # Przeniesienie na stronę wyboru kanapki
    # Użytkownik klika wyloguj
    # Przeniesienie na stronę główną, wyboru kanapki, bez użytkownika

    def tearDown(self):
        self.browser.close()
