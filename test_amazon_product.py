from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class TestAmazon:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="/Users/nicholasjames/PycharmProjects/automation_project/chromedriver")
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.amazon.com/")

    def test_amazon_product_search(self):
        search = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search.send_keys('ecobee smart thermostat', Keys.ENTER)

        smart_home = self.driver.find_element_by_xpath('//img[@alt="ecobee Lite SmartThermostat, Black"]')
        smart_home.click()

        ecobee_thermostat = self.driver.find_element_by_id('submit.add-to-cart')
        ecobee_thermostat.click()
        self.driver.implicitly_wait(10)

        checkout = self.driver.find_element_by_xpath('//input[@class="a-button-input"]')
        checkout.click()

    def teardown_method(self):
        self.driver.back()
        self.driver.quit()




