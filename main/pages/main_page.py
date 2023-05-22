import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    url = 'https://www.rukodelov.ru/'

    # locators

    embroidery = '/html/body/div[9]/div/div[3]/div[1]/a/div[2]'

    # getters

    def get_embroidery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.embroidery)))

    # actions

    def click_embroidery(self):
        self.get_embroidery().click()
        print('click embroidery')

    # methods

    def select_embroidery_category(self):
        with allure.step("Select embroidery category"):
            Logger.add_start_step(method="select_embroidery_category")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_embroidery()
            Logger.add_end_step(url=self.driver.current_url, method="select_embroidery_category")
