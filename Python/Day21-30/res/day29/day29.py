"""
    发邮件

"""

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email = ''
password = ''
receive_email = []
smtp_server = ''
smtp_port = None

def email_send():
    """
        发邮件
    """

    email = MIMEMultipart()# 创建邮件

    email['from'] = send_email# 发件人
    email['to'] = ', '.join(receive_email)# 收件人
    email['subject'] = Header('测试邮件', 'utf-8')# 邮件标题

    # 正文
    connect = '测试邮件内容,独立密码设置独立密码后，进入邮箱需要输入独立密码验证，使用QQ邮箱更加安全'
    email.attach(MIMEText(connect, 'plain', 'utf-8'))

    # 创建SMTP_SSL对象（连接邮件服务器)
    smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    smtp.login(send_email, password)

    smtp.sendmail(send_email, receive_email, email.as_string())
    smtp.quit()
    pass

def email_send_with_file():
    """
        发带附件的邮件
    """

    email = MIMEMultipart()# 创建邮件
    email['from'] = send_email# 发件人
    email['to'] = ', '.join(receive_email)# 收件人
    email['subject'] = Header('测试邮件', 'utf-8')
    connect = '测试邮件内容,独立密码设置独立密码后，进入邮箱需要输入独立密码验证，使用QQ邮箱更加安全'
    email.attach(MIMEText(connect, 'plain', 'utf-8'))

    with open('../20210803202628.png', 'rb') as f:
        """选择文件并指定编码"""
        file = MIMEText(f.read(), 'base64', 'utf-8')# 创建邮件附件
        file['Content-Type'] = 'image/png'# 指定文件类型
        file['Content-Disposition'] = 'attachment; filename="20210803202628.png"' # 指定文件名
        email.attach(file)

    smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    smtp.login(send_email, password)

    smtp.sendmail(send_email, receive_email, email.as_string())
    smtp.quit()
    pass


def text_message():
    pass

def main():
    # email_send()
    email_send_with_file()
    pass

if __name__ == '__main__':
    main()