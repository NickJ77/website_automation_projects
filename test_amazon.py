import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.mark.usefixtures()
class TestAmazon():
      def test_setup(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(7)
        driver.get("https://www.amazon.com/")
        driver.maximize_window()
        time.sleep(4)
        yield
        driver.quit()

     def test_search(self, test_setup):
        search_product = driver.find_element_by_id ("twotabsearchtextbox")
        search_product.send_keys('ecobee smart thermostat')
        search_product.send_keys(Keys.ENTER)
        time.sleep(4)
        thermostat = driver.find_element_by_xpath("//img[@alt='ecobee Smart Thermostat with Voice Control - Black.RFB (Renewed)']")
        thermostat.click()

     def test_add_to_cart(self, test_setup):
        cart_button = driver.find_element_by_id("add-to-cart-button")
        cart_button.click()
        time.sleep(4)
        actual_text = driver.find_element_by_xpath("//h1[@class='a-size-medium a-text-bold']").text
        expected_text = "Added to Cart"
        assert actual_text == expected_text, f'Error, Expected text: {expected_text}, but actual text: {actual_text}'











