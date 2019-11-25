from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/topics/19832')
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_0728(self):
        #self.driver.find_element(By.CSS_SELECTOR, '.title [title*="SoloPi："]').click()
        # time.sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, '.fa.fa-list').click()
        # self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default').click()
        self.driver.find_element_by_css_selector('.fa.fa-list').click()
        time.sleep(3)

        #元素定位没有报错，但是就是点不中
        # self.driver.find_element(By.XPATH, '(//ul/li[contains(@class,"toc-level-2")])[2]').click()
        #元素定位错误，上面定位的是li标签，实际上应该定位li标签下面的a标签
        self.driver.find_element(By.XPATH, '(//ul/li[contains(@class,"toc-level-2")])[2]/a').click()
        time.sleep(3)
