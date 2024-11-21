import allure,random,time
from Public.Base import web二次封装
@allure.feature('海盗电商系统后台增加商品')
class Test_haidao_reg_case:
    def setup_method(self):
        self.浏览器=web二次封装('chrome')
        
    def teardown_method(self):
        self.浏览器.关闭浏览器()
        
        
    @allure.story('增加商品测试001')  #要单个功能点
    @allure.title('验证正确的商品增加001')  #用例标题
    @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    def test_商品增加测试001(self):
        with allure.step('步骤1:打开后台地址'):
            self.浏览器.打开地址('http://129.204.147.168/haidao/index.php?m=admin&c=public&a=login')
        with allure.step('步骤2:登陆后台'):
            self.浏览器.输入内容('name','username','admin')
            self.浏览器.输入内容('name','password','qsq261719')
            self.浏览器.点击元素('name','dosubmit')
        with allure.step('步骤3:完成增加商品信息内容'):
            sp='商品'+str(random.randint(1000,9999))+str(random.randint(100,999))
            
            self.浏览器.点击元素('text','商品')
            self.浏览器.切换框架('name','main_frame')
            self.浏览器.点击元素('text','添加')
            self.浏览器.输入内容('name','name',sp)#商品名称
            self.浏览器.点击元素('xpath','/html/body/div[2]/form/div[2]/div[3]/div/div/div[1]/input[1]') #商品品牌
            self.浏览器.点击元素('xpath','/html/body/div[2]/form/div[2]/div[3]/div/div/div[3]/span[1]') #点击威图
            self.浏览器.点击元素('xpath','/html/body/div[2]/form/div[1]/div/div/input[2]')#点击选择
            self.浏览器.切换默认框架()
            
            self.浏览器.切换框架('xpath','/html/body/div[6]/div/table/tbody/tr[2]/td/div/iframe')
            self.浏览器.点击元素('xpath',' /html/body/div/div[1]/div[1]/a[1]')  #点击智能手机
            self.浏览器.点击元素('id','okbtn')  #点击确定
            self.浏览器.切换默认框架()
            
            self.浏览器.切换框架('name','main_frame')
            self.浏览器.输入内容('name','subtitle','牛b!') #广告语
            self.浏览器.输入内容('name','keyword','手机')  #商品关键词
            self.浏览器.输入内容('name','description','苹果手机就是贵，买不起！')  #商品描述
            self.浏览器.切换默认框架()

            time.sleep(2)
            self.浏览器.切换框架('name','main_frame')
            self.浏览器.点击元素('id','release')#点击下一步
            self.浏览器.输入内容('name','shop_price[]','8888')  # 然后再输入100
            self.浏览器.输入内容('name','market_price[]','9999')
            self.浏览器.输入内容('name','number[]','50')
            time.sleep(2)

            self.浏览器.点击元素('name','dosubmit')#点击下一步
            time.sleep(2)
            self.浏览器.点击元素('name','dosubmit')#点击下一步

            self.浏览器.点击元素('xpath','/html/body/div[2]/form/div[1]/div/div/div/div[1]/input')#选择商品属性
            self.浏览器.点击元素('xpath','/html/body/div[2]/form/div[1]/div/div/div/div[2]/span[2]')#选择手机
            time.sleep(2)
            self.浏览器.点击元素('id','goods_attr')#点击下一步
            self.浏览器.输入内容('xpath','/html/body/div[2]/div/form/div[1]/div[2]/div','66666666666666666')
            self.浏览器.点击元素('xpath','/html/body/div[2]/div/form/div[2]/input')#提交
            aa=self.浏览器.获取文本('xpath','/html/body/div/div/div[2]/span')#获取文本
            with allure.step('步骤4:断言商品增加成功'):
                实际结果=aa
                预期结果='操作成功！'
                assert 实际结果==预期结果
        print("商品名称:",sp)
                
    @allure.story('商品购买测试002')  #要单个功能点
    @allure.title('验证正确的商品购买001')  #用例标题
    @allure.description('用例描述,填写用例的详细数据,确保这些数据之前不存在系统')  #用例描述
    @allure.severity(allure.severity_level.CRITICAL)  #用例等级
    def test_商品购买测试001(self):
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
            time.sleep(5)
        with allure.step('步骤4:断言注册成功'):
            实际结果=self.浏览器.获取文本('xpath','/html/body/div[1]/div/ul[2]/li[1]/a')
            预期结果=username
            assert 实际结果==预期结果
        
        with allure.step('步骤5:购买商品'):
            self.浏览器.点击元素('text','返回商城首页')
            #商品购买                    
            self.浏览器.点击元素('xpath','/html/body/div[6]/div[1]/div/ul/li[1]/div[1]/a/img') #点击图片
            self.浏览器.点击元素('text','立即购买')
            self.浏览器.点击元素('xpath','/html/body/div[3]/div[2]/dl[1]/dd/div/a') #添加地址
            
            self.浏览器.切换框架('xpath','/html/body/div[7]/div/table/tbody/tr[2]/td/div/iframe')
            self.浏览器.点击元素('xpath','/html/body/form/div[1]/ul/li[1]/div/div/div[2]/div[1]') #收获地址
            self.浏览器.点击元素('text','广西')
            self.浏览器.点击元素('text','南宁')
            self.浏览器.点击元素('text','西乡塘')
            self.浏览器.点击元素('text','西乡塘街道')
            self.浏览器.输入内容('name','address','榕华大厦花椒青年公寓')
            self.浏览器.输入内容('name','name','王五')
            self.浏览器.输入内容('name','mobile','13888858974')
            self.浏览器.输入内容('name','zipcode','530000')
            self.浏览器.点击元素('id','hold')
            self.浏览器.切换默认框架()
            time.sleep(2)
            self.浏览器.点击元素('text','货到付款')
            self.浏览器.输入内容('xpath','/html/body/div[3]/div[2]/div[1]/div/div[1]/div/input','速速发货')
            self.浏览器.点击元素('text','提交订单')
            订单号=self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div[1]/p[1]/span')

            time.sleep(2)
            with allure.step('步骤6:断言商品购买成功'):
                实际结果=self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div[1]/p[1]/span')
                预期结果=订单号
                assert 实际结果==预期结果
            print(订单号)