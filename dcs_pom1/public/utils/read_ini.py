
'''
此模块是用来封装读取ini文件的工具类
python当中通过configparser这个模块当中Configparser类来读取ini文件
如果没有configparser则需要下载安装：
在dos窗口输入：  pip install configparser
或者通过：python -m pip install configparser
'''
from configparser import ConfigParser   #导入configparser模块中ConfigParser类
from conf.cms_path import *          #从config模块导入所有的路径
import os
class Read_Ini(ConfigParser):   #定义了一个类，继承了ConfigParser类里面的方法和属性

    def __init__(self,filename):
        super(Read_Ini,self).__init__()  #继承了父类的构造方法
        self.filename=filename
        self.read(self.filename)      #读取ini文件

    def read_data_ini(self,section=None, option=None):
        '''
        封装一个获取section对应的option里面的value值
        :return:
        '''
        value = self.get(section,option)   #通对应的option拿到value值
        return value
file = os.path.join(conf_path,"conf.ini")
read = Read_Ini(file)
url = read.read_data_ini("test_data","url")
print(url)















