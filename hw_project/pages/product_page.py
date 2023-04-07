import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ProductPage(Base):

    # locators

    price = '//*[@id="smartfilter"]/form/div[1]/div[1]'
    slider = '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div/div/div/div/div/div[2]/div/span[2]'
    confirm = '//*[@id="smartfilter-apply-block"]/a'
    type = '//*[@id="smartfilter"]/form/div[7]/div[1]'
    cross_stitch = '//*[@id="smartfilter"]/form/div[7]/div[2]/div/div/div[2]/ul/li[3]'
    in_stoke = '//*[@id="smartfilter"]/form/div[12]'
    product_1 = '/html/body/div[8]/div/div[2]/div/div[3]/div[3]/div[3]/div[1]/div[1]/div/div[1]/div/div[5]/button[1]'
    popup = '//*[@id="coupon-popup"]/div/div/a'
    cart = '//*[@id="rkd-header-actions"]/a[4]/span[2]/span[2]'

    # getters

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider)))

    def get_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm)))

    def get_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type)))

    def get_cross_stitch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cross_stitch)))

    def get_in_stoke(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.in_stoke)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_popup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # actions

    def scroll_to_price(self):
        price1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))
        ActionChains(self.driver).move_to_element(price1).perform()
        print('move to price')

    def click_price(self):
        self.get_price().click()
        print('click price')

    def move_slider(self):
        slider1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider)))
        ActionChains(self.driver).click_and_hold(slider1).move_by_offset(-130, 0).release().perform()
        print('move to slider')

    def click_confirm(self):
        self.get_confirm().click()
        print('click confirm')

    def scroll_to_type(self):
        type1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type)))
        ActionChains(self.driver).move_to_element(type1).perform()
        print('move to type')

    def click_type(self):
        self.get_type().click()
        print('click type')

    def click_cross_stitch(self):
        self.get_cross_stitch().click()
        print('click category cross stitch')

    def scroll_to_in_stoke(self):
        in_stoke1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.in_stoke)))
        ActionChains(self.driver).move_to_element(in_stoke1).perform()
        print('move to in stoke')

    def click_in_stoke(self):
        self.get_in_stoke().click()
        print('click in stoke')

    def click_product_1(self):
        self.get_product_1().click()
        print('click product_1')

    def click_popup(self):
        self.get_popup().click()
        print('click popup')

    def click_cart(self):
        self.get_cart().click()
        print('click cart')

    # methods

    def select_product(self):
        self.get_current_url()
        self.driver.execute_script('window.scrollTo(0, 50)')
        self.scroll_to_price()
        self.click_price()
        self.move_slider()
        self.click_confirm()
        self.scroll_to_type()
        self.click_type()
        self.click_cross_stitch()
        self.click_confirm()
        self.scroll_to_in_stoke()
        self.click_in_stoke()
        self.click_product_1()
        self.click_popup()
        self.click_cart()


