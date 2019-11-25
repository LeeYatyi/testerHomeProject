from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def find(self, locator, value=None) -> WebElement:
        if value == None:
            return self._driver.find_element(*locator)
            # return WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        else:
            return self._driver.find_element(locator, value)
            # return \
            #     WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located((locator, value)))

    def click_by_js(self, by, locator):
        """
        :param by:
        :param locator:
        :return:
        """
        # 显式等待
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))
        self._driver.execute_script("arguments[0].click();", self._driver.find_element(by, locator))


    # def waitinfo(self, by, locator):
    #     return (self._driver, 10).until(expected_conditions.visibility_of_element_located((by,locator)))
