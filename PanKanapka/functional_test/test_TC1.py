from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase

from time import sleep

WEB_ADDRESS = 'http://127.0.0.1:8000'

class RegistrationTest(TestCase):
    #Użytkownik otwiera przeglarkę
    def setUp(self):
        self.browser = webdriver.Firefox()
    # Użytkownik wchodzi na stronę główną
    def test_get_registration_site(self):
        self.browser.get(WEB_ADDRESS)
        # Użytkownik klika zaloguj
        self.browser.find_element_by_link_text('Login').click()
        # Użytkownik jest przeniesiony na stronę logowania
        header_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Podaj email i hasło', header_text)

        # Użytkownik wpisuje dane do logowania (email, hasło) i klika zaloguj
        input_user_id = self.browser.find_element_by_id('id_username')
        input_user_id.send_keys('test@test.pl')
        input_password_id = self.browser.find_element_by_id('id_password')
        self.assertEqual('password', input_password_id.get_attribute('type'))
        input_password_id.send_keys('test')
        sleep(2)
        all_buttons = self.browser.find_elements_by_tag_name('button')
        self.browser.find_element_by_class_name('btn-lg2').click()
        # Przeniesienie na stronę wyboru kanapki
        # Użytkownik klika wyloguj
        # Przeniesienie na stronę główną, wyboru kanapki, bez użytkownika

    def tearDown(self):
        self.browser.close()
