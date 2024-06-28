
from public.pages.BasePage import BasePage  #导入BasePage
from selenium import webdriver
from public.utils.read_ini import read  #导入read对象
import unittest
from public.pages.pages_element import Pages_Element as p


url = read.read_data_ini("test_data","url")
username = read.read_data_ini("test_data","username")
pwd = read.read_data_ini("test_data","pwd")

class Test_login(BasePage):
    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Chrome()   #创建一个唯一的driver
        BasePage.set_driver(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        '''每次跑完用例等待3秒'''
        BasePage.sleep(3)

    def test_01_login(self):
        #1.拿到driver对象
        driver = BasePage.get_driver()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)

        #2.输入用户名

        elem =BasePage.find_element(p.userName)
        BasePage.sendKeys(elem,username)

        #3.输入密码

        elem = BasePage.find_element(p.passWord)
        BasePage.sendKeys(elem,pwd)

        #4.点击登陆

        elem = BasePage.find_element(p.loginBtn)
        BasePage.click(elem)

        #5.断言

        value =BasePage.get_text(p.desktop)
        assert value=="我的桌面"


if __name__ == '__main__':
    unittest.main()



























