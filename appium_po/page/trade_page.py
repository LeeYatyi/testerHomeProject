from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage


class TradePage(BasePage):
    _a_open = (MobileBy.ACCESSIBILITY_ID, 'A股开户')

    def goto_hs(self):
        self.driver.find_element_by_xpath('//*[@text="沪深"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self._a_open))
        return self

    def a_open(self):
        sleep(5)
        self.driver.find_element(self._a_open).click()
        return self