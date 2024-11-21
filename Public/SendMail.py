"""
邮件服务器:smtp.qq.com
发信人:1838516970@qq.com
收信人:1838516970@qq.com
邮件主题:python自动化测试报告-2024-12-01
附件:
端口号:465
授权码:pxmsmixxpmaicgge 
"""

import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#导入MIMEApplication类，用于创建附件
from email.mime.application import MIMEApplication

def send_mail(filepath, tomail):
    #创建一个MIMEMultipart对象
    msg = MIMEMultipart()
    #设置邮件主题
    msg.attach(MIMEText(open(filepath, 'rb').read(), 'html', 'utf-8'))
    #构造附件
    htmlpart = MIMEApplication(open(filepath, 'rb').read())
    htmlpart.add_header('Content-Disposition', 'attachment', filename=filepath)
    #设置附件的文件名
    msg.attach(htmlpart)
    #构造邮箱信息
    msg['Subject'] = f'python自动化测试报告-{time.strftime('%Y-%m-%d')}'
    msg['From']= '1838516970@qq.com'
    msg['To'] = tomail
    #发送邮件
    try:
        #连接到SMTP服务器
        smtp = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
        #登录邮箱
        smtp.login(user='1838516970@qq.com', password=  'pxmsmixxpmaicgge')
        smtp.sendmail(from_addr='1838516970@qq.com', to_addrs=tomail, msg=msg.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(f'邮件发送失, 原因是{e}')
    #关闭SMTP连接
    smtp.quit()
if __name__ == '__main__':
    import os
    print(os.getcwd())
    send_mail('./Report/report_2024_11_11_11_10_32.html', '1838516970@qq.com')