from test_selenium.test_wework import Department


class TestDepartment:
    def test_list(self):
        department = Department()
        r = department.list("")
        assert department.list("")["errcode"] == 0

    def test_create(self):
        pass
    


