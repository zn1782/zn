
from conf.cms_path import *
import time
import unittest
from public.utils.HTMLTestRunnerNew import HTMLTestRunner

#定义生成报告的路径以及文件名称
now = time.strftime('%Y-%m-%d-%H-%M-%S')
# print(now)
filename = report_path + "\\" + str(now) + "_ui_report.html"
# print(filename)

def auto_run():
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,
                                                   pattern="test_*.py")
    f = open(filename,"wb")
    runner = HTMLTestRunner(stream=f,
                            title="Cms后台系统UI自动化测试报告",
                            description="用例执行情况如下",
                            tester="dcs")
    runner.run(discover)
    f.close()  #关闭文件

if __name__ == '__main__':
    auto_run()














