

'''
此模块是用来读取excel表格的工具类
读取exce表格需要用到xlrd模块
dos窗口输入：pip install xlrd
'''
import xlrd
from conf.cms_path import *
import os
class Read_Excel(object):

    def __init__(self,filename,sheet_Name):
        #先打开一个excel表格
        self.workbook=xlrd.open_workbook(filename)
        #进入到sheet页面
        self.sheetName=self.workbook.sheet_by_name(sheet_Name)

    def get_excel_data(self,row,col):
        '''
        封装了一个通过行和列来获取excel表格里面数据的工具方法
        '''
        value = self.sheetName.cell(row,col).value
        return value
file = os.path.join(data_path,"data.xlsx")   #把data的路径和data.xls文件名进行拼接
excel = Read_Excel(file,"cms_data")
url = excel.get_excel_data(1,0)  #根据索引去取第二行第一列的url地址
print(url)

#
# import openpyxl   #操作Excel表格的库
# from conf.cms_path import *
# import os
# class R_Excel(object):
#     '''封装一个班读取Excel表格的工具类'''
#     def __init__(self,filename,sheet_name):
#         self.filename = filename
#         self.sheet_name = sheet_name
#     def open(self):
#         '''封装一个打开Excel表格的工具方法'''
#         #通过openpyxl模块调用load_workbook函数打开filename文件
#         self.wb = openpyxl.load_workbook(self.filename)
#         # 通过self.wb这个Excel文件的对象读取对应的sheet页面的
#         self.sh = self.wb[self.sheet_name]
#     def read_data(self,row,col):
#         self.open()
#         cell = self.sh.cell(row=row, column=col)
#         return cell.value
# if __name__ == '__main__':
#     file = os.path.join(data_path,"data.xlsx")   #把data的路径和data.xls文件名进行拼接
#     excel = R_Excel(file,"cms_data")
#     url = excel.read_data(1,1)  #根据索引去取第二行第一列的url地址
#     print(url)
















