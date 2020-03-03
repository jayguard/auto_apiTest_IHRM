# 导包
import unittest, logging, app

import pymysql
import requests
from api.emp_api import EmployeeApi
from utils import assert_utils


# 创建测试类集成unittest.TestCase
class TestEmployee(unittest.TestCase):

    # 初始化unittest的函数
    def setUp(self):
        # 实例化EmployeeApi
        self.emp_handle = EmployeeApi()

    def tearDown(self):
        pass

    def test_01_login(self):
        # 调用登陆
        response = self.emp_handle.login("13800000002", "123456")
        # 打印登陆结果
        logging.info("员工模块的登陆结果为：{}".format(response.json()))
        # 取出令牌，并拼接成以Bearer 开头的字符串
        token = "Bearer " + response.json().get('data')
        logging.info("取出的令牌为：{}".format(token))
        # 设置员工模块所需要的请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        # 保存请求头到app.py中的HEADERS中
        app.HEADERS = headers
        self.HEADERS = headers
        logging.info("员工模块请求头为：{}".format(self.HEADERS))

    def test_02_add_emp(self):
        # 调用添加员工
        response_add_emp = self.emp_handle.add_emp("王健林suar35376",
                                                "16732323667",
                                                app.HEADERS)
        logging.info("添加员工接口的结果为：{}".format(response_add_emp.json()))
        # 断言：响应状态码，success，code，message
        assert_utils(self, response_add_emp, 200, True, 10000, "操作成功")
        # 由于添加员工成功后，还需要保存员工ID给后续的查询、修改、删除员工使用，所以我们需要保存员工ID
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMPID = emp_id
        logging.info("保存的员工ID为：{}".format(app.EMPID))

    def test_03_query_emp(self):
        # 调用查询员工
        response_query = self.emp_handle.query_emp(app.EMPID, headers=app.HEADERS)
        logging.info("查询员工的结果为：{}".format(response_query.json()))
        # 断言：响应状态码，success，code，message
        assert_utils(self, response_query, 200, True, 10000, "操作成功")

    def test_04_modify_emp(self):
        # 调用修改员工
        response_modify = self.emp_handle.modify_emp(app.EMPID, "new_tom", headers=app.HEADERS)
        logging.info("修改员工结果为：{}".format(response_modify.json()))
        # 建立连接 username：readuser
        # password：iHRM_user_2019
        conn = pymysql.connect(host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 执行SQL语句
        # 根据添加员工返回的id查询数据库中员工表的username，这样就能获取到修改之后的数据
        sql = "select username from bs_user where id = {}".format(app.EMPID)
        logging.info("要查询的SQL语句为：{}".format(sql))
        # 执行查询的sql语句
        cursor.execute(sql)
        # 获取返回结果
        result = cursor.fetchall()
        logging.info("SQL查询出来的结果为：{}".format(result))  # ('new_tom',)
        # 断言修改结果是否正确
        # 注意：如果是用fetchall()取出的数据，那么取出result时，需要有两个下表result[0][0]
        self.assertEqual("new_tom", result[0][0])
        # 关闭连接
        cursor.close()
        # 关闭游标
        conn.close()
        # 断言：响应状态码，success，code，message
        assert_utils(self, response_modify, 200, True, 10000, "操作成功")

    def test_05_delete_emp(self):
        # 调用删除员工
        response_delete = self.emp_handle.delete_emp(app.EMPID, app.HEADERS)
        logging.info("删除员工的结果为：{}".format(response_delete.json()))
        # 断言：响应状态码，success，code，message
        assert_utils(self, response_delete, 200, True, 10000, "操作成功")
