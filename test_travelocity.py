from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestTravelocity():
    def demo_vacation(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.travelocity.com/')
        destination = driver.find_element_by_xpath("//button[@aria-label='Going to']")
        destination.send_keys('Orlando')
        search = driver.find_element_by_xpath("//button[normalize-space()='Search']")
        search.click()


searchlocation = TestTravelocity()
searchlocation.demo_vacation()
