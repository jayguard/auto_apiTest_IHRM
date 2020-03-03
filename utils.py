# 自定义工具类
import json

import pymysql


# 封装通用断言函数
from app import BASE_DIR


def assert_common_utils(self, response, http_code, success, code, message):
    # 断言响应状态码，success，code，message的值
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 封装数据库
class DBUtils:

    # 初始化类时，要运行的代码
    def __init__(self, host="182.92.81.159", user='readuser', password='iHRM_user_2019', database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 代表使用with语法时，进入函数时会先运行enter的代码
    def __enter__(self):
        # 与数据库建立连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        # 获取游标
        self.cusor = self.conn.cursor()
        return self.cusor

    # 代表退出with语句块时，会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标和关闭连接
        if self.cusor:
            self.cusor.close()
        if self.conn:
            self.conn.close()


def get_test_data(file_path):
    with open(file_path, encoding='utf-8') as f:
        read_data = json.load(f)
        data_list = []
        for i in read_data.values():
            data_list.append(tuple(i.values()))

    return data_list

# 封装通用断言函数
def assert_utils(self, response, http_code, success, code, message):
    # 断言响应状态码，success，code，message的值
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

