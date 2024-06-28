class Pages_Element():

    #1.输入用户名
    userName = ("id", "userAccount")

    #2.输入密码
    passWord = ("id", "loginPwd")

    #3.点击登陆
    loginBtn = ("id", "loginBtn")

    #4.断言
    desktop = ("xpath", "/html/body/div/section/div[1]/div[1]/ul/li/span")

    # 5.点击用户中心
    user_center = ("xpath",'//*[@id="menu-user"]/dt')

    #6.点击用户管理
    user_manager = ("link_text","用户管理")

    #7.定位外层iframe框
    iframe = ("xpath","/html/body/div/section/div[2]/div[2]/iframe")

    #8.点击添加用户
    user_add = ("partial","添加用户")
