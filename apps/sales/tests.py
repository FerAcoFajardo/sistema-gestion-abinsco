from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

# Create your tests here.

class SalesTestCase(TestCase):

    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #super(test_sales, cls).tearDownClass()
    
    def setUp(self):
        driver = self.driver

        #driver.get('http://127.0.0.1:8000/')
        driver.get('http://localhost:8000/')

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        
        submit = driver.find_element_by_id('submitBtn')
        
        username.send_keys('admin')
        password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source

    def test_normal_sale_without_credit(self):
        driver = self.driver

        driver.get('http://localhost:8000/sales/create')
        

        select_product = Select(driver.find_element_by_id('id_form-__prefix__-product'))

        btn_add_product = driver.find_element_by_id('add-form')

        select_product.select_by_value('1')

        btn_add_product.send_keys(Keys.RETURN)


        select_product.select_by_value('2')

        btn_add_product.send_keys(Keys.RETURN)

        quantity_first_product = driver.find_element_by_id('cart-index-0')

        quantity_first_product.send_keys(Keys.ARROW_UP)
        quantity_first_product.send_keys(Keys.ARROW_UP)

        submit = driver.find_element_by_id('submit-btn')

        submit.send_keys(Keys.RETURN)

        time.sleep(5)

        #customer = driver.find_element_by_css_selector("#s2id_customer .select2-choice")
        #customer = driver.find_element_by_xpath("//span[@class='selection']")
        #customer.click()

        #time.sleep(5)

        #customer.select_by_value('1')


        #assert "Ventas" in driver.title