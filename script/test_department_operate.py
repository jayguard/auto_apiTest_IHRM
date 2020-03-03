import logging
import unittest

import app
from api.department_api import DepartmentApi
from api.emp_api import EmployeeApi
from utils import assert_utils


class Test_department(unittest.TestCase):
    def setUp(self):
        self.depart = DepartmentApi()
        self.emp_handle = EmployeeApi()
        # 查/改/删的id:
        self.query_id = "1234481661672271872"
        self.modify_id = "1234481661672271872"
        self.delete_id = "1234481661672271872"

        # 调用登陆
        response = self.emp_handle.login("13800000002", "123456")
        # 取出令牌，并拼接成以Bearer 开头的字符串
        token = "Bearer " + response.json().get('data')
        # 设置员工模块所需要的请求头
        self.headers = {"Content-Type": "application/json", "Authorization": token}
        # 保存请求头到app.py中的HEADERS中
        logging.info("员工模块请求头为：{}".format(self.headers))



    def tearDown(self):
       pass


    def test_01_add_department(self):
        response =self.depart.add_dep("影子520", "2020", self.headers)
        print("添加部门结果:{}".format(response.json()))
        assert_utils(self, response, 200, True, 10000, "操作成功！")


    def test_02_query_department(self):
        response = self.depart.query_dep(id=self.query_id, headers=self.headers)
        print("部门查询结果:{}".format(response.json()))
        assert_utils(self, response, 200, True, 10000, "操作成功！")

    #
    def test_03_modify_department(self):
        response = self.depart.modify_dep(id=self.modify_id, headers=self.headers, name="影子200", code="2020")
        print("部门修改结果:{}".format(response.json()))
        assert_utils(self, response, 200, True, 10000, "操作成功！")

    def test_04_delete_department(self):
        response = self.depart.delete_dep(id=self.delete_id, headers=self.headers)
        print("部门删除结果:{}".format(response.json()))
        assert_utils(self, response, 200, True, 10000, "操作成功！")




