import os
import win32com.client as win32
import datetime
import readConfig
import getpathInfo
from common.Log import logger
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



read_conf = readConfig.ReadConfig()
mailSmtpServer = read_conf.get_email('mailSmtpServer')
mailSmtpUser = read_conf.get_email('mailSmtpUser')
mailSmtpPwd = read_conf.get_email('mailSmtpPwd')
mailTitle = read_conf.get_email('mailTitle')
mailBody = read_conf.get_email('mailBody')#从配置文件中读取，邮件主题
mailAppType = str(read_conf.get_email('mailAppType'))#从配置文件中读取，邮件类型
mailFromPerson = str(read_conf.get_email('mailFromPerson'))
mailToPerson = read_conf.get_email('mailToPerson')#从配置文件中读取，邮件收件人
mailToCC = read_conf.get_email('mailToCC')#从配置文件中读取，邮件抄送人
mailFilePath = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
logger = logger

class send_email():
    def mail(self):
        try:
            # 创建一个实例
            with open(mailFilePath,'rb') as f:
                mailBody = f.read()
            message = MIMEMultipart()
            message.attach(MIMEText(mailBody, 'html', 'utf-8'))  # 邮件正文
            message['From'] = mailFromPerson  # 邮件上显示的发件人
            message['To'] = mailToPerson  # 邮件上显示的收件人
            message['Subject'] = Header(mailTitle, 'utf-8')  # 邮件主题
            att1 = MIMEText(open(mailFilePath, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="report.html"'
            message.attach(att1)

            smtp = smtplib.SMTP()  # 创建一个连接
            smtp.connect(mailSmtpServer)  # 连接发送邮件的服务器
            smtp.login(mailSmtpUser, mailSmtpPwd)  # 登录服务器
            smtp.sendmail(mailFromPerson, message['To'].split(','), message.as_string())  # 填入邮件的相关信息并发送
            logger.info("邮件发送成功！！！")
            smtp.quit()
        except smtplib.SMTPException:
            logger.info("邮件发送失败")


if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
    send_email().mail()
    logger.info("send email ok!!!!!!!!!!")