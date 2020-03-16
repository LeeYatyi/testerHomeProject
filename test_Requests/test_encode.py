import base64
import json
import requests


class TestEncode:
    original_url = 'http://127.0.0.1:10000/topics.json'
    url = 'http://127.0.0.1:10000/topics_base64.json'
    def test_get(self):
        res = requests.get(self.original_url)
        assert len(res.json()['topics']) == 2

    def test_encode(self):
        res = requests.get(self.url)
        data = self.decode_base64(res.content)
        json_data = json.loads(data)
        assert len(json_data['topics']) == 2

    def decode_base64(self, raw):
        return base64.b64decode(raw)

    def test_api(self):
        req = ApiRequest()
        req_data = {
            "schema": "http",
            "method": "GET",
            "url": self.url,
            "headers" : None,
            "encoding": "base64"
        }
        res = req.send(req_data)
        assert len(res["topics"]) == 2

class ApiRequest:
    def send(self, data: dict):
        if data['schema'] == "http":
            res = requests.request(data['method'], data['url'], headers=data['headers'])
            if data['encoding'] == "base64":
                return json.loads(base64.b64decode(res.content))
            else:
                return json.loads(res.content)
        elif data['schema'] == "dubbo":
            pass
        elif data['schema'] == "websoket":
            pass
        else:
            pass
