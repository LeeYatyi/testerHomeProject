import logging
from time import sleep, time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)
class TestSelenium:
    def setup(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.debugger_address="127.0.0.1:9999"

        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.get('https://testerhome.com')

    def teardown(self):
        self.driver.quit()

    def test_form_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("seveniruby@testerhome.com")

        self.driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#user_remember_me").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#new_user > div.from-group.checkbox > label")
        logging.info(element.is_displayed())
        logging.info(element.id)
        logging.info(element.tag_name)
        logging.info(element.text)
        logging.info(element.location)
        logging.info(element.size)
        logging.info(element.rect)
        logging.info(element.get_attribute("for"))

        self.driver.find_element(By.NAME, "commit").click()
        # sleep(30)




