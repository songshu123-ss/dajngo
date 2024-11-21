"""
冒烟测试,开发人员每次提交代码,都需要进行冒烟测试,确保最基本的功能是可用的
"""
from Public.Base import web二次封装
import time

class Test_haidaocase:
    def setup_method(self):
        self.浏览器 = web二次封装('chrome')
    
    def teardown_method(self):
        self.浏览器.关闭浏览器()
        
        

    def test_登陆测试001(self):
        """验证正确的用户名密码登录的功能"""
        self.浏览器.打开地址('http://129.204.147.168/haidao') # 调用方法
        self.浏览器.点击元素('text','登录')
        self.浏览器.输入内容('name','username','admin')
        self.浏览器.输入内容('name','password','qsq261719')
        self.浏览器.点击元素('id','popup-submit')
        time.sleep(2)
        实验结果=self.浏览器.获取文本('xpath','/html/body/div[1]/div/ul[2]/li[1]/a')
        assert 实验结果=='admin'
        
        
    def test_登陆测试002(self):
        """验证错误的用户名密码登录的功能"""
        self.浏览器.打开地址('http://129.204.147.168/haidao') # 调用方法
        self.浏览器.点击元素('text','登录')
        self.浏览器.输入内容('name','username','admin')
        self.浏览器.输入内容('name','password','123456525343')
        self.浏览器.点击元素('id','popup-submit')
        
        实际结果=self.浏览器.获取文本('class','error')
        assert 实际结果=='用户不存在或密码错误'