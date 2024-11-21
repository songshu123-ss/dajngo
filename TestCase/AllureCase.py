import allure,random,time
from Public.Base import web二次封装
from Public.DB import 数据库操作类

@allure.feature('海盗电商系统注册模块')
class Test_haidao_reg_case:
    def setup_method(self):
        self.浏览器=web二次封装('chrome')
        
    def teardown_method(self):
        self.浏览器.关闭浏览器()
        
        
    @allure.story('注册测试001')  #要单个功能点
    @allure.title('验证正确的信息注册001')  #用例标题
    @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    def test_登陆测试001(self):
        with allure.step('步骤1:打开系统地址'):
            self.浏览器.打开地址('http://129.204.147.168/haidao')
        with allure.step('步骤2:点击注册按钮'):
            self.浏览器.点击元素('text', '注册')
        with allure.step('步骤3:填写注册信息'):
            username='laowang'+str(random.randint(1000,9999))+str(random.randint(100,999))
            self.浏览器.输入内容('name','username',username)
            self.浏览器.输入内容('name','password','123123')
            self.浏览器.输入内容('name','pwdconfirm','123123')
            self.浏览器.输入内容('name','email',str(random.randint(1000,9999))+"123456@qq.com")
            self.浏览器.输入内容('name','mobile',"176"+str(random.randint(10000000,99999999)))
            self.浏览器.点击元素('name','dosubmit')
            time.sleep(2)
        with allure.step('步骤4:断言注册成功'):
            实际结果=self.浏览器.获取文本('xpath','/html/body/div[1]/div/ul[2]/li[1]/a')
            预期结果=username
            assert 实际结果==预期结果
        
        with allure.step('步骤5:断言数据库中存在'):
            mysql=数据库操作类('129.204.147.168', 3306, 'root', '', 'hd')
            mysql.连接mysql数据库()
            sql='select count(1) from hd_member where username="'+username+'"' 
            result=mysql.执行查询语句(sql)
            print(result)
            mysql.关闭数据库连接()
            assert result[0][0]==1
            
            
    @allure.story('注册测试002(用户名)')  #要单个功能点
    @allure.title('验证错误的信息注册002')  #用例标题
    @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    def test_登陆测试002(self):
        with allure.step('步骤1:打开系统地址'):
            self.浏览器.打开地址('http://129.204.147.168/haidao')
        with allure.step('步骤2:点击注册按钮'):
            self.浏览器.点击元素('text', '注册')
        with allure.step('步骤3:填写错误的用户名注册信息'):
            self.浏览器.输入内容('name','username','ab')
            self.浏览器.点击元素('name','password')
            time.sleep(1)
        with allure.step('步骤4:断言注册成功'):
            实际结果=self.浏览器.获取文本('class','validform_checktip')
            预期结果='用户名长度在3-15个字符'
            assert 实际结果==预期结果
            
            
    # @allure.story('注册测试003(密码)')  #要单个功能点
    # @allure.title('验证错误的信息注册003')  #用例标题
    # @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    # @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    # def test_登陆测试003(self):
    #     with allure.step('步骤1:打开系统地址'):
    #         self.浏览器.打开地址('http://129.204.147.168/haidao')
    #     with allure.step('步骤2:点击注册按钮'):
    #         self.浏览器.点击元素('text', '注册')
    #     with allure.step('步骤3:填写错误的密码注册信息'):
    #         self.浏览器.输入内容('name','username','abc')
    #         self.浏览器.输入内容('name','password','1234')
    #         self.浏览器.点击元素('name','pwdconfirm')
    #         time.sleep(1)
    #     with allure.step('步骤4:断言注册成功'):
    #         实际结果=self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[2]/div/span')
    #         预期结果='密码至少为 6 位字符'
    #         assert 实际结果==预期结果
            
            
            
            
    # @allure.story('注册测试004(确认密码)')  #要单个功能点
    # @allure.title('验证错误的确认密码004')  #用例标题
    # @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    # @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    # def test_登陆测试004(self):
    #     with allure.step('步骤1:打开系统地址'):
    #         self.浏览器.打开地址('http://129.204.147.168/haidao')
    #     with allure.step('步骤2:点击注册按钮'):
    #         self.浏览器.点击元素('text', '注册')
    #     with allure.step('步骤3:填写错误的密码注册信息'):
    #         self.浏览器.输入内容('name','username','abc')
    #         self.浏览器.输入内容('name','password','123456')
    #         self.浏览器.输入内容('name','pwdconfirm','15648787465')
    #         self.浏览器.点击元素('name','email')
    #         time.sleep(1)
    #     with allure.step('步骤4:断言注册成功'):
    #         实际结果=self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[3]/div/span')
    #         预期结果='两次输入的内容不一致！'
    #         assert 实际结果==预期结果
            
            
            
    # @allure.story('注册测试005(邮箱)')  #要单个功能点
    # @allure.title('验证错误的邮箱005')  #用例标题
    # @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    # @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    # def test_登陆测试005(self):
    #     with allure.step('步骤1:打开系统地址'):
    #         self.浏览器.打开地址('http://129.204.147.168/haidao')
    #     with allure.step('步骤2:点击注册按钮'):
    #         self.浏览器.点击元素('text', '注册')
    #     with allure.step('步骤3:填写错误的密码注册信息'):
    #         self.浏览器.输入内容('name','username','abc')
    #         self.浏览器.输入内容('name','password','123456')
    #         self.浏览器.输入内容('name','pwdconfirm','123456')
    #         self.浏览器.输入内容('name','email','123mbjhbln')
    #         self.浏览器.点击元素('name','mobile')
    #         time.sleep(1)
    #     with allure.step('步骤4:断言注册成功'):
    #         实际结果=self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[4]/div/span')
    #         预期结果='邮箱地址格式不对！'
    #         assert 实际结果==预期结果
            
            
            
    # @allure.story('注册测试006(邮箱)')  #要单个功能点
    # @allure.title('验证错误的邮箱006')  #用例标题
    # @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    # @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    # def test_登陆测试006(self):
    #         with allure.step('步骤1:打开系统地址'):
    #             self.浏览器.打开地址('http://129.204.147.168/haidao')
    #         with allure.step('步骤2:点击注册按钮'):
    #             self.浏览器.点击元素('text', '注册')
    #         with allure.step('步骤3:填写错误的密码注册信息'):
    #             self.浏览器.输入内容('name','username','abc')
    #             self.浏览器.输入内容('name','password','123456')
    #             self.浏览器.输入内容('name','pwdconfirm','123456')
    #             self.浏览器.输入内容('name','email','123mbjhbln@qq.com')
    #             self.浏览器.输入内容('name','mobile','1807878')
    #             self.浏览器.点击元素('id','popup-submit')
    #             time.sleep(1)
    #         with allure.step('步骤4:断言注册成功'):
    #             实际结果=self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[5]/div/span')
    #             预期结果='请填写正确的手机号码！'
    #             assert 实际结果==预期结果