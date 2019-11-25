from time import time, sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage


class ProfilePage(BasePage):
    def update(self, **kwargs):
        self.click_by_js(By.CSS_SELECTOR, ".ww_operationBar .js_edit")
        # element = self._driver.find_element(By.NAME, "username")
        element = self.find((By.NAME, "username"))
        element.clear()
        element.send_keys(kwargs["name"])
        self.click_by_js(By.CSS_SELECTOR, ".js_save")
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "js_tips")))

    def disable(self):
        self.click_by_js(By.CSS_SELECTOR, '.js_disable')
        sleep(3)
        # self.click_by_js(By.XPATH, '//a[@d_ck="cancel"]')
        self.click_by_js(By.XPATH, '//a[@d_ck="submit"]')


    def enable(self):
        self.click_by_js(By.CSS_SELECTOR, '.js_disable')
        sleep(3)
        # self.click_by_js(By.XPATH, '//a[@d_ck="cancel"]')

    def delete(self):
        pass

    def invite(self):
        pass

