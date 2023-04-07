import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    # locators

    name_product_1_cart = '//*[@id="basket-item-3018010"]/div[2]/div[2]/div[1]/a'
    checkout_button = '//*[@id="basket-root"]/div/div[3]/div[3]/div/div[2]/button'
    one_click = '//*[@id="bx-soa-method"]/div[2]/div/div[1]/div[3]/div/input'
    name = '//*[@id="soa_oneclick_name"]'
    telephone = '//*[@id="soa_oneclick_phone"]'

    # getters

    def get_name_product_1_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_1_cart)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_one_click(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.one_click)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    # actions

    def scroll_to_checkout(self):
        checkout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
        ActionChains(self.driver).move_to_element(checkout).perform()
        print('move to checkout_button')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('click checkout button')

    def click_one_click(self):
        self.get_one_click().click()
        print('click oneclick button')

    def input_name(self, user_name):
        self.get_name().send_keys(user_name)
        print('input user name')

    def input_telephone(self, telephone_number):
        self.get_telephone().send_keys(telephone_number)
        print('input telephone number')

    # methods

    def confirm_order(self):
        self.get_current_url()
        self.assert_url('https://www.rukodelov.ru/personal/order/make/?')
        self.scroll_to_checkout()
        self.click_checkout_button()
        time.sleep(5)
        self.click_one_click()
        self.input_name('Иван Петрович')
        self.input_telephone('891111111')
        # self.click_checkout_button()  # accept order
        self.get_screenshot()
