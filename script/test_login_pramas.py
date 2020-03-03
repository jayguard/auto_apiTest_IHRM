# 导包
import unittest, logging, app

import pymysql
import requests
from parameterized import parameterized

from api.emp_api import EmployeeApi
from utils import assert_utils, get_test_data


test_data = get_test_data(app.BASE_DIR + "/data/login.json")
# 创建测试类集成unittest.TestCase
class TestLogin(unittest.TestCase):

    # 初始化unittest的函数
    def setUp(self):
        # 实例化EmployeeApi
        self.emp_handle = EmployeeApi()

    def tearDown(self):
        pass

    @parameterized.expand(test_data)
    def test_01_login(self, mobile, password, http_code, success, code, message):
        # 调用登陆
        response = self.emp_handle.login(mobile, password)
        # 打印登陆结果
        logging.info("员工模块的登陆结果为：{}".format(response.json()))
        assert_utils(self, response, http_code, success, code, message)