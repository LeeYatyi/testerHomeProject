from unittest import TestCase

from test_wework.utils.Utils import Utils


class TestUtils:
    def test_format(self):
        r = Utils.json_format({"a": 1, "b": {"c": "xxx"}})
        print(r)
        print(type(r))

