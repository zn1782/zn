import  os

#项目路径
base_path=os.path.dirname(os.path.dirname(__file__))
print(base_path)
#conf 路径
conf_path=os.path.join(base_path,'conf')
print(conf_path)
#定义data路径
data_path = os.path.join(base_path,"data")
print(data_path)
#定义pages路径
pages_path = os.path.join(base_path,"public","pages")
print(pages_path)
#定义utiles路径
utiles_path = os.path.join(base_path,"public","utiles")
print(utiles_path)
#定义report路径
report_path = os.path.join(base_path,"report")
print(report_path)
#定义：testcase路径
testcase_path = os.path.join(base_path,"testcase")
print(testcase_path)
#定义：run路径
run_path = os.path.join(base_path,"run")
print(run_path)