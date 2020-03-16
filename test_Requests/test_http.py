#coding=utf-8
import json
import requests
from requests import Response
from jsonpath import jsonpath
from jsonschema import validate

class TestHTTP:
    def test_get(self):
        url = "http://47.95.238.18:8090/post"
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {'a': "2", "bcd": "header demo", "accept": "application/json"}

        r = requests.get(url, params=payload, headers=headers)
        self.inspect_response(r)

    def test_post(self):
        url = "http://47.95.238.18:8090/post"
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {'a': "2", "bcd": "header demo", "accept": "application/json"}
        proxies = {'http': 'http://127.0.0.1:8888'}
        # data/json
        r = requests.post(url, json=payload, headers=headers)
        self.inspect_response(r)

    def inspect_response(self, r: Response):
        print(r.headers)
        print(r.cookies)
        print(r.status_code)
        print(r.encoding)
        print(r.url)
        print(r.content)
        print(r.text)
        print(r.raw)
        print(r.json())


    def test_xueqiu_search(self):
        url = "https://xueqiu.com/stock/search.json"
        params = {'code': 'sougou', 'size': 3, 'page': 1}
        header = {'Accept': 'application/json',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                  'Cookie': 'xq_a_token=a664afb60c7036c7947578ac1a5860c4cfb6b3b5'}
        r = requests.get(url, params=params, headers=header)
        print(r.json())
        assert r.json()['stocks'][0]['name'] == '搜狗'

    def test_get_login_jsonpath(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        print(data['topics'])
        assert jsonpath(data, "$.topics[?(@.user.login == 'gentle-yu')].user.id")[0] == 47924

    def test_get_login_jsonschema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema1.json", encoding='utf-8'))
        validate(data, schema=schema)

    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {'corpid':'wwc1c217a5b5458dd3', 'corpsecret': 'P9EscwSnpRBKDV29RAy8L-2NtBwqUUESv7xfj4Aapv8'}
        res = requests.get(url, params=params)
        print(res.json())



