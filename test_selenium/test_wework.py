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
        # 进入已经打开的chrome进程
        # 进入chrome.exe路径，在dos下运行chrome.exe --remote-debugging-port=9222
        # 链接调试开关打开的chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address="127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=chrome_options,)
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()

    def test_upload_file(self):
        element_add = self.driver.find_element_by_css_selector('.js_upload_file_selector')
        element_add.click()
        sleep(3)
        # element_upload = self.driver.find_element_by_css_selector("#js_upload_input")
        # js执行，避免元素点击不生效
        # self.driver.execute_script('arguments[0].click()', element_upload)
        # 通过上传图片路径达到上传图片效果
        self.driver.find_element_by_css_selector("#js_upload_input").send_keys(r"E:\照片\壁纸\1.jpg")
        # sleep(3)
        # 打印页面元素
        print(self.driver.page_source)
        # 显示等待：等待图片上传完毕
        WebDriverWait(self.driver,5).until(expected_conditions.invisibility_of_element_located(
            (By.CSS_SELECTOR,".js_uploadProgress_cancel")
        ))
        self.driver.find_element_by_css_selector(".js_next").click()
        sleep(3)

    def test_add_member(self):
        # element_add = self.driver.find_element_by_css_selector(("a.qui_btn.ww_btn.js_add_member"))
        # element_add.click()
        # sleep(3)
        elements = self.driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_add_member")
        elements[1].click()
        # 上传图片
        # element_upload_file = self.driver.find_element_by_id('js_upload_file')
        # self.driver.execute_script('arguments[0].click()',element_upload_file)
        self.driver.find_element_by_id('js_upload_file').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"选择图片")]/input').send_keys(r"E:\照片\壁纸\2.jpg")
        # 等待上传完毕
        locator_reload = '//a[contains(text(),"重新上传")]'
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_reload)))

        self.driver.find_element(By.CSS_SELECTOR,'.js_save').click()
        # 等待保存成功
        locator_save = 'js_tips'
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, locator_save)))
        #打印页面元素
        # print(self.driver.page_source)

        self.driver.find_element_by_css_selector("input#username").send_keys("张三")
        self.driver.find_element_by_xpath('//*[@name="acctid"]').send_keys("test001")
        self.driver.find_element_by_xpath('//input[@value="2" and @name="gender"]').click()
        self.driver.find_element_by_css_selector('#memberAdd_phone').send_keys('12345678901')
        sleep(3)

