from time import sleep

from test_po.manager_page import ManagerPage
from test_po.wework_page import Wework


class TestManager:
    def setup(self):
        self.work = Wework()
        self.manager = ManagerPage(self.work)
        # self._driver.find_element_by_id('menu_manageTools').click()

    def teardown(self):
        sleep(5)
        self.work.quit()

    def test_goto_picture(self):
        self.manager.goto_image()

    def test_add_image(self):
        self.manager.goto_image().add_image(r"E:\照片\壁纸\1.jpg")
