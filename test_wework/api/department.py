import requests

from test_selenium.test_wework import WeWork


class Department:
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    creat_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

    def list(self, id):
        r = requests.get(self.list_url,params={"access_token":WeWork.get_token(),"id": id}).json()
        return r

    def creat(self,name,parentid,order):
        r = requests.post(self.creat_url, params={"access_token":WeWork.get_token()}, json={"name":name,"parentid":parentid,"order":order,"id":""}).json()
        return r

    def delete(self):
        pass