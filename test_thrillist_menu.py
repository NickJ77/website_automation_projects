import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestThrillist:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.thrillist.com/")
        driver.maximize_window()
        time.sleep(4)
        yield
        driver.quit()

    def test_menu_funtionality(self, test_setup):
        cities = driver.find_element_by_xpath('//a[@href="/eat"]')
        cities.click()
        eat = driver.find_element_by_xpath('//a[@href="/drink"]')
        eat.click()
        drink = driver.find_element_by_xpath('//a[@href="/travel"]')
        drink.click()
        travel = driver.find_element_by_xpath('//a[@href="/weed"]')
        travel.click()
        cannabis = driver.find_element_by_xpath('//a[@href="/entertainment"]')
        cannabis.click()
        watch = driver.find_element_by_xpath('//a[@href="/shopping"]')
        watch.click()
        shop = driver.find_element_by_xpath('//a[@href="https://www.thrillist.com/newsletters"]')
        shop.click()

