# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver


class TestXueqiu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("image_cancel").click()
        self.driver.find_element_by_id("user_profile_icon")

    def setup(self):
        pass

    def teardown(self):
        self.driver.find_element_by_id("action_close").click()

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    def test_profile(self):
        self.driver.find_element_by_id("user_profile_icon").click()
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_open")
        # el1.click()
        # el2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # el2.click()
        # el3 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # el3.click()
        # el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
        # el4.click()

    def test_swipe(self):
        self.driver.swipe(500, 900, 100, 200, 1000)

    @pytest.mark.parametrize("keyword, stock_type, expect_price", [("alibaba", 'BABA', 170), ('xiaomi', '01810', 8.5)])
    def test_search(self, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
            "//*[contains(@resource-id, 'current_price')]").text)
        print(price)
        assert price > expect_price
