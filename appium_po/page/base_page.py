from appium.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator, value=None) -> WebElement:
        if value == None:
            return self.driver.find_element(*locator)
            # return WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        else:
            return self.driver.find_element(locator, value)
