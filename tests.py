from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LoginFormTestCase( LiveServerTestCase):
    
    def testForm(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        
        submit = driver.find_element_by_id('submitBtn')
        
        username.send_keys('admin')
        password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source