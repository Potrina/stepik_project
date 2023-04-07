import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('./chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('start test')

    mp = MainPage(driver)
    mp.select_embroidery_category()

    pp = ProductPage(driver)
    pp.select_product()

    cp = CartPage(driver)
    cp.confirm_order()

    print('finish test')
    time.sleep(10)
    driver.quit()
