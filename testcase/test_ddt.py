#coding=utf-8
import unittest

from ddt import ddt, data, file_data, unpack

from src.myfunc import add, divide,is_prime

import yaml


#from HtmlTestRunner import HTMLTestRunner
#from HTMLTestRunner import HTMLTestRunner   #执行结果生成HTML报告

@ddt
class TestMyFunc(unittest.TestCase):
    '''test myfunc.py'''
    '''
    def setUp(self):
        print "每个用例执行前会调用setUp方法准备环境"

    def tearDown(self):
        print "每个用例执行前会调用tearDown方法清理环境"
    '''

    @classmethod
    def setUpClass(cls):
        print("所有用例执行前会调用一次setUp方法准备环境")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行前会调用一次tearDown方法清理环境")

    @data(5, 7,8,-2,0,1)
    def test_is_prime(self, a):    #测试用例以test_开头
        ''' test method is_prime(number) '''
        print("is_prime")
        self.assertFalse(is_prime(a))    #不适合多种断言测试
        # self.assertTrue(is_prime(value))
        # self.assertFalse(is_prime(value))
        # self.assertFalse(is_prime(value))
        # self.assertFalse(is_prime(value))
        # self.assertFalse(is_prime(value))

    @data((3,1,2),(4,2,2),(0,-1,1))
    @unpack
    def test_add(self,a,b,c):
        '''test method add(a,b)'''
        print("add")
        self.assertEqual(a, add(b,c))
        # self.assertNotEqual(3, add(2,2))

    @file_data('myfunc.yaml')
    def test_divide(self,a,b,c):
        '''test method divide(a,b)'''
        print("divide")
        self.assertEqual(a,divide(b,c))
        # self.assertNotEqual(2,divide(6,2))

if __name__ == "__main__":
    unittest.main()
#     '''
#     问题1： 如何控制用例执行顺序
#     在unittest中，用例是以test开头的方法定义的，默认执行顺序是根据用例名称升序进行，如上面的用例，实际执行顺序为：test_add-->test_divide-->test_is_prime,而不是用例定义的先后顺序。
#     问题2：如何让多个用例共用setup、teardown
#     unittest的setup、teardown会在每个用例执行前后执行一次，如上面测试用例类中有3个测试用例，那么每个用例执行前会执行setup，执行后会执行teardown，即setup、teardown总共会调用三次，但考虑实际自动化测试场景，多个用例只需执行一次setup，全部用例执行完成后，执行一次teardown，针对该种场景，unittest的处理方法是使用setupclass、teardownclas,注意@classmethod的使用
#     问题3：如何跳过用例
#     在自动化测试中，经常会遇到挑选用例的情况，在unittest中的解决方法是使用skip装饰器，其中skip装饰器主要有3种：unittest.skip(reason)、unittest.skipIf(condition,reason)、unittest.skipUnless(condition,reason)，即在满足condition条件下跳过该用例，reason用于描述跳过的原因
#     问题4：如何生成html格式的测试报告
#     Unittest中默认生成的报告格式为txt，如果想生成html格式的报告，可以使用HtmlTestRunner模块，安装后导入该模块，使用HTMLTestRunner代替默认的TextTestRunner()执行测试用例即可。
#     '''
#     #1、可用TestSuite控制用例顺序，用例的执行顺序由添加到TestSuite中的顺序决定
#     tests = [TestMyFunc("test_is_prime"), TestMyFunc("test_add"), TestMyFunc("test_divide")]
#     suite = unittest.TestSuite()
#     suite.addTests(tests)   #将测试用例实例添加到测试套件
#
#
#     with open('result.txt','w+') as f:
#         # 创建测试运行器（TestRunner），将测试报告输出到文件中
#         runner = unittest.TextTestRunner(stream=f, verbosity=2)
#         runner.run(suite)
#
#
#     '''
#     #with open("result.html", "w+") as report:
#         runner = HTMLTestRunner(stream=report, descriptions=True, verbosity=2)
#         runner.run(suite)
#     '''
#
#     #runner = HTMLTestRunner(output="result", descriptions=True, verbosity=2, report_title="Test Report")
#     #runner.run(suite)

