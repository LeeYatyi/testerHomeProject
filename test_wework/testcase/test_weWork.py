from test_wework.api.wework import WeWork


class TestWeWork:
    def test_get_token(self):
        wework = WeWork()
        token = wework.get_token()
        assert token != None
