import pymysql
from Public.Logs import 日志记录类
class 数据库操作类:
    def __init__(self,host, port, user, password, db):
        self.log = 日志记录类()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
    def 连接mysql数据库(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
            self.cur = self.conn.cursor()
            self.log.info('数据库连接成功,主机:'+self.host)
        except Exception as e:
            print('数据库连接失败,错误信息:', e)
            self.log.error('数据库连接失败,错误信息:' +str(e))
    def 执行查询语句(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.log.info('查询语句为' +sql+ '查询结果为:'+str(data))
        return data

    def 关闭数据库连接(self):
        self.cur.close()
        self.conn.close()
        self.log.info('数据库连接已关闭')
        

if __name__ == '__main__':
    db = 数据库操作类('129.204.147.168/', 3306, 'root', '', 'hd')
    db.连接mysql数据库()
    sql = 'select count(*) from ha_member where username="admin"' 
    result = db.执行查询语句(sql)
    print(result)
    db.关闭数据库连接()
    
    
    
    
    
'''
select 需要的列名 from 表名 where 条件 group by 分组 having 条件 order by 排序 limit 限制
聚合运算:count()数数行 sum()求列的和 avg()求列的平均 max()求列的最大值 min()求列最小值

海盗表:
hd_member  注册用户信息表
hd_order  订单表
hd_goods_sku  商品表
'''
