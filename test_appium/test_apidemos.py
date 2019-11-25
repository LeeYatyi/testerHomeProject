# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver

class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        #caps['autoGrantPermissions'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        sleep(2)

    def teardown(self):
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
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*0.8, height*0.8, width*0.2, height*0.2, 1000)
        self.driver.find_element_by_accessibility_id("Views").click()
        sleep(3)
        for i in range(5):
            self.driver.swipe(width*0.8, height*0.8, width*0.2, height*0.2, 1000)

    def test_uiautomator(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView('
            'new UiSelector().text("Views").instance(0))').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView('
            'new UiSelector().text("Tabs").instance(0))').click()
