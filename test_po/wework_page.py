from selenium import webdriver


class Wework:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'
        self.driver.get(url)
        cookies = {
            # "wwrtx.vst": "MUdOAIYx4q91EAZP89hNmOsfEWApqL6moaUioIlOKcjqOCOd_vGBia9BdUrr7TAzHHmqidYpa9ZLRA-fUWgqAQ82Or6BxHEix3BU4JQ-ZgTrCLqjekaTTqSfi850eRnOQCMba4qLOlO2Fp88Dg7dZluVb8Wdt5Ng6Y5uflniSjiBUgFRL6P8Fdmgb74h2hjdK6EmY2gFcx8NVJDutTvIwxqw09rVoRFyxgca_UDQqeKIsUS8nQQVMd1M15ZRchpjIyrbMWMwRfbI7RIfTgHK-w",
            "wwrtx.d2st": "a6276727",
            "wwrtx.sid": "s-_r9Bhuj_ilwrtDyQjn8Pz5ImxGs8w2nXq_kQSBCnGi9_xCLbYd0C9f2UHuiFF4",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325086089236",
            "wxpay.vid": "1688850429824195",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()
