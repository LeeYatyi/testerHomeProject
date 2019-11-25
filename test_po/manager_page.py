from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.image_page import ImagePage
from test_po.wework_page import Wework


class ManagerPage(BasePage):
    def __init__(self, wework: Wework):
        self._driver = wework.driver

    def goto_image(self):
        # self._driver.find_element_by_xpath('//div[contains(text(),"素材库")]').click()
        self.click_by_js(By.XPATH, '//div[contains(text(),"素材库")]')
        self.click_by_js(By.CSS_SELECTOR, '.ww_icon_GrayPic')
        return ImagePage(self._driver)

