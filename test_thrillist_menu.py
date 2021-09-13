from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class TestThrillist:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="/Users/nicholasjames/PycharmProjects/automation_project/chromedriver")
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.thrillist.com/")

    def test_thrillist_menu(self):
        self.driver.find_element_by_xpath('//a[@href="/eat"]').click()
        self.driver.find_element_by_xpath('//a[@href="/drink"]').click()
        self.driver.find_element_by_xpath('//a[@href="/travel"]').click()
        self.driver.find_element_by_xpath('//a[@href="/weed"]').click()
        self.driver.find_element_by_xpath('//a[@href="/entertainment"]').click()
        self.driver.find_element_by_xpath('//a[@href="/shopping"]').click()

    def test_thrillist_footer(self):
        self.driver.find_element_by_xpath('//a[@href="https://www.thrillist.com/newsletters"]').click()

    def teardown_method(self):
        self.driver.back()
        self.driver.quit()

