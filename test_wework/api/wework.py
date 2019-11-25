import requests


class WeWork:
    corpid = "wwd6da61649bd66fea"
    AgentId = "1000010"
    agent_secret = "pAF_eP3FlN3d6 - GxGFESaEwL1G5or1UQmHjkc9rtTj8"
    contact_secret = "C7uGOrNyxWWzwBsUyWEbLdbZBDrc71PNOhyQ_YYPhts"
    access_token = None

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url,params={"corpid": self.corpid, "contact_secret": self.contact_secret}).json()
        access_token = r["access_token"]
