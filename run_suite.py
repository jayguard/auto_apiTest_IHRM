import time
import unittest


from HTMLTestRunner import HTMLTestRunner

from app import BASE_DIR
from script.test_login_pramas import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
report_file = BASE_DIR + "/report/login_test_report_{}.html".format(time.strftime("%Y-%m-%d %H%M"))
with open(report_file, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title="iHRM系统登陆接口测试", description="实现方式: 数据驱动")
    #verbosity:设置的参数可以标记用例执行的结果
    runner.run(suite)