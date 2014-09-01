# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailManager:
    def __init__(self):
        self.mail_info = {}
    
    def send_mail(self, mail_from, mail_to_list, subject, content):
        # 格式应该是这样的 Nickname<username@host.address>，中间无空格
        txt = MIMEText(content, 'html')  # 若content中有html编码
        # txt = MIMEText(content) # 若content中没有html编码
        txt.set_charset('utf-8')
        msg = MIMEMultipart()
        msg['Subject'] = subject
        # 格式为： Nickname<username@host.address>，中间无空格
        msg['From'] = 'Ever' + '<' + mail_from + '>'
        msg['To'] = ';'.join(mail_to_list)
        msg.attach(txt)
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_info['host'])
            s.login(self.mail_info['sender'], self.mail_info['sender_password'])
            s.sendmail(self.mail_info['sender_address'], mail_to_list, msg.as_string())
            s.close()
        except:
            return False
        return True
