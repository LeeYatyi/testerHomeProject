import requests

class WeWork:
    corpid = "wwc1c217a5b5458dd3"
    Agent_id = "1000002"
    agent_secret = "xfvnE_wTjDSK_sLG-M3HfHjiSo38RWScmZP--6k-T4A"
    contact_secret = "4W9nHhcRSGyIAJIDClsaAYZ0hIvHtshNxpyuhIT1cOg"
    access_token = None


    @classmethod
    def get_token(cls):
        if cls.access_token == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            resp = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.contact_secret}).json()
            cls.access_token = resp["access_token"]
            # print(resp)

        return cls.access_token
