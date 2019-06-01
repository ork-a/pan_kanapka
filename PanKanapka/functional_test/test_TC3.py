from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase

from time import sleep

WEB_ADDRESS = 'http://127.0.0.1:8000/'

class RegistrationTest(TestCase):
    #Użytkownik otwiera przeglarkę
    def setUp(self):
        self.browser = webdriver.Chrome("C:\_ZADANIA\pan_kanapka\chromedriver.exe")

    def login(self):
        self.browser.get(WEB_ADDRESS)
        self.browser.find_element_by_link_text('Login').click()
        input_user_id = self.browser.find_element_by_id('id_username')
        input_user_id.send_keys('test@test.pl')
        input_password_id = self.browser.find_element_by_id('id_password')
        input_password_id.send_keys('test')
        input_password_id.send_keys(Keys.ENTER)

    def skip_test_get_registration_site(self):

        current_page_url = self.browser.current_url
        self.assertEqual(current_page_url, WEB_ADDRESS)
        #komunikat o poprawnym logowaniu
        message = self.browser.find_element_by_class_name('messages').text
        self.assertIn('zalogowany', message)
        # Użytkownik klika wyloguj
        self.browser.find_element_by_link_text('Logout').click()
        # Przeniesienie na stronę główną, wyboru kanapki, bez użytkownika
        current_page_url = self.browser.current_url
        self.assertEqual(current_page_url, WEB_ADDRESS)
        # komunikat o poprawnym wylogowaniu
        message = self.browser.find_element_by_class_name('messages').text
        self.assertIn('wylogowany', message)

    def tearDown(self):
        self.browser.close()
