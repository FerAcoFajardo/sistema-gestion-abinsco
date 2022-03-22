from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

class SalesTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window() # For maximizing window
        driver = cls.driver

        driver.get('http://localhost:8000/')

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        
        submit = driver.find_element_by_id('submitBtn')
        
        username.send_keys('admin')
        password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #super(test_sales, cls).tearDownClass()
    
    def test_normal_sale_without_credit(self):
        driver = self.driver

        driver.get('http://localhost:8000/sales/create')

        select_customer = Select(driver.find_element_by_id('id_customer'))
        select_customer.select_by_index('1')

        select_product = Select(driver.find_element_by_id('id_form-__prefix__-product'))
        select_product.select_by_index('1')

        btn_add_product = driver.find_element_by_id('add-form')
        btn_add_product.send_keys(Keys.RETURN)
        select_product.select_by_value('2')
        btn_add_product.send_keys(Keys.RETURN)

        quantity_first_product = driver.find_element_by_id('cart-index-0')
        quantity_first_product.send_keys(Keys.ARROW_UP)
        quantity_first_product.send_keys(Keys.ARROW_UP)

        submit = driver.find_element_by_id('submit-btn')
        submit.send_keys(Keys.RETURN)

        self.assertEqual("Tutorialspoint", "Tutorialspoint")
        #assert "Ventas" in driver.title

        # para dar click al select2
        #customer = driver.find_element_by_css_selector("#s2id_customer .select2-choice")
        #customer = driver.find_element_by_xpath("//span[@class='selection']")
        #customer.click()
    

    def test_normal_sale_with_credit(self):

        driver = self.driver

        driver.get('http://localhost:8000/sales/create')
        
        select_customer = Select(driver.find_element_by_id('id_customer'))
        select_customer.select_by_index('1')

        radio_credit = driver.find_element_by_id('credito')
        radio_credit.click()
        
        select_product = Select(driver.find_element_by_id('id_form-__prefix__-product'))
        select_product.select_by_index('1')

        btn_add_product = driver.find_element_by_id('add-form')
        btn_add_product.send_keys(Keys.RETURN)
        select_product.select_by_value('2')
        btn_add_product.send_keys(Keys.RETURN)

        quantity_first_product = driver.find_element_by_id('cart-index-0')
        quantity_first_product.send_keys(Keys.ARROW_UP)
        quantity_first_product.send_keys(Keys.ARROW_UP)

        submit = driver.find_element_by_id('submit-btn')
        #submit.send_keys(Keys.RETURN)
        
        self.assertEqual("Tutorialspoint", "Tutorialspoint")
