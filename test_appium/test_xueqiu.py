# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "andriod demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_profile(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_open")
        # el1.click()
        # el2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # el2.click()
        # el3 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # el3.click()
        # sleep(2)
        self.driver.find_element_by_id("user_profile_icon").click()

