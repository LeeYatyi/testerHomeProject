from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.profile_page import ProfilePage
from appium_po.page.search_page import SearchPage
from appium_po.page.trade_page import TradePage


class XueqiuPage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        # WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located((By.ID,"image_cancel")))
        # self.driver.find_element_by_id("image_cancel").click()
        self.driver.find_element_by_id("user_profile_icon")

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        return ProfilePage(self.driver)

    def quit(self):
        sleep(10)
        self.driver.quit()

    def goto_trade(self):
        # WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located
        #     ((By.XPATH, '//*[@text="交易")]')))
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        return TradePage(self.driver)