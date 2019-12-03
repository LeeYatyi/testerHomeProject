
from appium_po.page.xueqiu_page import XueqiuPage


class TestTrade:
    def setup(self):
        self.xueqiu = XueqiuPage()
        # self.trade = self.xueqiu.goto_trade()
        # self.trade.goto_hs()

    def teardown(self):
        self.xueqiu.quit()

    def test_a_open(self):
        # self.trade.a_open("18911773181", "1234")
        self.xueqiu.goto_trade().goto_hs()