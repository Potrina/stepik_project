from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    url = 'https://www.rukodelov.ru/'

    # locators

    # catalog_button = '//li[@class="position-relative"]'
    # embroidery_category = '//a[@data-href="/catalog/nabory_dlya_vyshivaniya/"]'
    # embroidery_button = '//*[@id="rkd-header-dd-subcategory-2"]/div/div[1]/span[1]'

    embroidery = '/html/body/div[9]/div/div[3]/div[1]/a/div[2]'

    # getters

    # def get_catalog_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    #
    # def get_embroidery_category(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.embroidery_category)))
    #
    # def get_embroidery_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.embroidery_button)))

    def get_embroidery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.embroidery)))

    # actions

    # def click_catalog_button(self):
    #     self.get_catalog_button().click()
    #     print('click catalog button')
    #
    # def click_embroidery_category(self):
    #     self.get_embroidery_category().click()
    #     print('click embroidery category')
    #
    # def click_embroidery_button(self):
    #     self.get_embroidery_button().click()
    #     print('click embroidery button')

    def click_embroidery(self):
        self.get_embroidery().click()
        print('click embroidery')

    # methods

    def select_embroidery_category(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        # self.click_catalog_button()
        # self.click_embroidery_category()
        # self.click_embroidery_button()
        self.click_embroidery()

