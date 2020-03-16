from test_wework.api.department import Department
from test_wework.utils.Utils import Utils


class TestDepartment:
    def test_list(self):
        department = Department()
        department_list = department.list("")
        print(Utils.json_format(department_list))
        assert department_list["errcode"] == 0

    def test_create(self):
        pass

    def test_delete(self):
        pass

    def test_update(self):
        pass

    


