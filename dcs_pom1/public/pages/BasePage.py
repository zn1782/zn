
'''
此模块是封装所有用例的基类
比如说：所有用例要用到的元素定位，以及输入框输入，点击，下拉等等公共方法
'''
import unittest  #导入unittest 框架
from time import *
# 调试代码
from selenium import webdriver

class BasePage(unittest.TestCase):  #创建一个BasePage类，这个类继承unittest框架中TestCase这个类
    driver = webdriver.Chrome()
    @classmethod
    def set_driver(cls,driver):  #入参是一个driver对象，把创建好的driver对象传进来，变成BasePage这个类的属性
        #把传进来的谷歌浏览器对象作为当前类、基类属性，基类的变量
        cls.driver = driver
    @classmethod
    def get_driver(cls):   #单例设计模式
        return cls.driver

    @classmethod
    def find_element(cls,element):
        type = element[0]   #id
        value = element[1]  #kw
        if type == "id":
            elem = cls.driver.find_element_by_id(value)
        elif type == "xpath":
            elem = cls.driver.find_element_by_xpath(value)
        elif type == "class":
            elem = cls.driver.find_element_by_class_name(value)
        elif type == "name":
            elem = cls.driver.find_element_by_name(value)
        elif type == "css":
            elem = cls.driver.find_element_by_css_selector(value)
        elif type == "link_text":
            elem = cls.driver.find_element_by_link_text(value)
        elif type == "partial":
            elem = cls.driver.find_element_by_partial_link_text(value)
        else:
            raise ValueError("plese input corrt paramters")
        return elem

    @classmethod   #封装输入函数
    def sendKeys(cls,elem,text):  #返回elem，根据实际业务封装
        return elem.send_keys(text)

    @classmethod   #封装点击操作
    def click(cls,elem):
        return elem.click()

    @classmethod
    def wait(cls,sec):
        '''封装一个隐式等待'''
        return driver.implicitly_wait(sec)

    @classmethod
    def sleep(cls,sec):
        return sleep(sec)

    @classmethod
    def frame(cls,elem):
        '''定位iframe框'''
        return cls.driver.switch_to.frame(elem)

    @classmethod
    def outframe(cls):
        return cls.driver.switch_to.default_content()

    @classmethod
    def get_text(cls,element):
        '''封装根据网页元素拿到text值'''
        value = BasePage.find_element(element).text
        return value

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    baidu_input = ("id","kw")
    elem = BasePage.find_element(baidu_input).send_keys("多测师")
    # elem = BasePage.find_element(baidu_input)
    # BasePage.sendKeys(elem,"多测师")





















































