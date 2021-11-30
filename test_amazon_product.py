import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest


class TestAmazon:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(7)
        driver.get("https://www.amazon.com/")
        driver.maximize_window()
        time.sleep(4)
        yield
        driver.quit()

    def test_search(self, test_setup):
        search_product = driver.find_element_by_id("twotabsearchtextbox")
        search_product.send_keys('ecobee smart thermostat')
        search_product.send_keys(Keys.ENTER)
        time.sleep(4)
        thermostat = driver.find_element_by_xpath("//img[@alt='ecobee Smart Thermostat with Voice Control - Black.RFB (Renewed)']")
        thermostat.click()

    def test_menu_bar(self, test_setup):
        best_sellers = driver.find_element_by_xpath("//div[@id='nav-xshop']//a[contains(@class,'')][normalize-space()='Best Sellers']")
        best_sellers.click()
        amazon_basics = driver.find_element_by_xpath("//a[normalize-space()='Amazon Basics']")
        amazon_basics.click()
        epic_daily_deals = driver.find_element_by_xpath("//a[normalize-space()='Epic Daily Deals']")
        epic_daily_deals.click()
        customer_service = driver.find_element_by_xpath("//a[normalize-space()='Customer Service']")
        customer_service.click()






