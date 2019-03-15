import smtplib
import sys
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class EmailSender(object):
    def __init__(self, host, username, password, port=25):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.email = smtplib.SMTP()

        self.__connect()
        self.__login()

    def __connect(self):
        try:
            self.email.connect(self.host, self.port)
            sys.stdout.write("Success Connect! " + "\n")
        except:
            sys.stderr.write("Failed To Connect! " + "\n")

    def __login(self):
        try:
            self.email.login(self.username, self.password)
            sys.stdout.write("Success Login! " + "\n")
        except:
            sys.stderr.write("Failed To Login! " + "\n")

    # # 添加附件
    # def __addannex(self, logs):
    #     for log in logs.keys():
    #         try:
    #             textpart = MIMEApplication(open(logs[log], 'rb').read())
    #             if log == "report":
    #                 textpart.add_header('Content-Disposition', 'attachment', filename=log + ".html")
    #             else:
    #                 textpart.add_header('Content-Disposition', 'attachment', filename=log + ".text")
    #             self.message.attach(textpart)
    #         except:
    #             print(log + " not exist")
    def add_message(self, html_file):
        # TODO（koushushin）: 将使用爬虫爬下来allure生成测试报告的网页，保存在某个路径，再发送报告
        # with open(html_file, 'rb') as f:
        #     msg_text = f.read()
        #     f.close()
        msg_text = ""
        msg = MIMEText(msg_text, 'html', 'utf-8')
        self.message = MIMEMultipart()
        self.message.attach(msg)

    def add_header(self, s_from, s_to, s_subject):
        self.message['from'] = s_from
        self.message['to'] = s_to
        self.message['subject'] = Header(s_subject, 'utf-8')

    def send(self, sender, receivers):
        try:
            self.email.sendmail(sender, receivers, self.message.as_string())
            sys.stdout.write("Success Send Email! " + "\n")
        except e:
            sys.stderr.write("Failed To Send Email" + "\n" + e)



if __name__ == '__main__':
    e = EmailSender("smtp.163.com",'17611263070@163.com', 'Test12345', 25)
    e.add_message(None)
    e.add_header("17611263070@163.com", "yusei1098340607@163.com", "dante sender")
    e.send("17611263070@163.com", "yusei1098340607@163.com")

