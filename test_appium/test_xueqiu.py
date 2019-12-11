# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        # caps['aotumationName'] = 'UiAutomator'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id("image_cancel").click()
        self.driver.find_element_by_id("user_profile_icon")

    def setup(self):
        pass
    #
    # def teardown(self):
    #     self.driver.find_element_by_id("action_close").click()

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

    @pytest.fixture()
    def search_fixture(self):
        print("setup search_fixture")
        sleep(2)
        yield
        self.driver.find_element_by_id("action_close").click()

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

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        for i in range(30):
            sleep(2)
            print(self.driver.context)
        # print(self.driver.page_source)
        # sleep(10)
        # #
        # # WebDriverWait(self.driver, 10,1).until(lambda x: "WEBVIEW_com.xueqiu.android" in self.driver.contexts)
        # #
        # print("====webview load===")
        # print(self.driver.page_source)
        # #
        # sleep(10)
        # # # self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        # print("====webview enter===")
        # print(self.driver.page_source)

    def test_screenshot(self):
        self.driver.start_recording_screen()
        self.driver.save_screenshot("home.png")
        trade = self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]')
        trade.screenshot("trade.png")
        trade.click()
        # self.driver.orientation
        sleep(10)
        self.driver.stop_recording_screen()

    def test_log(self):
        print(self.driver.log_types)
        print(self.driver.get_log("logcat"))

    def test_netwok(self):
        """
        - adb shell
        - ls /sdcard/snowball/image_cache/
        - exit
        - adb pull /sdcard/snowball/image_cache/16eabd0a6da17f2d3fe915e1.mp4 /tmp/1.mp4
        # 备注：在cmd窗口下可运行，在gitbash下报错
        :return:
        """
        self.driver.send_sms("18911773181", "hello world")
        sleep(3)
        self.driver.make_gsm_call("18911773181", "call")
        sleep(5)

    def test_perf(self):
        print(self.driver.get_performance_data_types())
        perf_data = self.driver.get_performance_data_types()
        sleep(10)
        # adb shell dumpsys cpuinfo \| grep "com.xueqiu.android"
        for p in perf_data:
            print("%s + info :" % p)
            print(self.driver.get_performance_data("com.xueqiu.android", p))

