from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage
from test_po.wework_page import Wework


class ImagePage(BasePage):
    _upload = (By.CSS_SELECTOR, '.js_upload_file_selector')
    _input = (By.CSS_SELECTOR, '#js_upload_input')
    _cancel = (By.CSS_SELECTOR, ".js_uploadProgress_cancel")
    _next = (By.CSS_SELECTOR, '.js_next')

    def add_image(self, path):
        # element_add = self._driver.find_element_by_css_selector('.js_upload_file_selector')
        # element_add.click()
        self.click_by_js(*self._upload)
        # element_upload = self.driver.find_element_by_css_selector("#js_upload_input")
        # js执行，避免元素点击不生效
        # self.driver.execute_script('arguments[0].click()', element_upload)
        # 通过上传图片路径达到上传图片效果
        # self._driver.find_element_by_css_selector("#js_upload_input").send_keys(path)
        self.find(*self._input).send_keys(path)
        # sleep(3)
        # 打印页面元素
        # print(self._driver.page_source)
        # 显示等待：等待图片上传完毕
        WebDriverWait(self._driver, 5).until(expected_conditions.invisibility_of_element_located(self._cancel))
        # self._driver.find_element_by_css_selector(".js_next").click()
        self.click_by_js(*self._next)
        sleep(3)

