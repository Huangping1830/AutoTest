#coding:utf-8
import smtplib
from email.mime.text import MIMEText
'''
发送邮件 smtplib
邮件格式 

'''
class SendEmail:
    global send_user
    global email_host
    global password
    email_host = 'smtp.163.com'
    send_user = "huangping183@163.com"
    password = 'HP69852087'
    def send_mail(self,user_list,sub,content):#收件人，主题，内容
        user = "huangping" + "<"+ send_user + ">"  #发件人
        message = MIMEText(content,_subtype='plain',_charset='utf-8')  #构建邮件格式
        #连接邮箱服务器
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ';'.join(user_list)  #str.json()
        server = smtplib.SMTP()  #邮件服务器
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        #90%
        pass_result = "%.2f%%" %(pass_num/count_num*100)#取小数点后两位 + %
        fail_result = "%.2f%%" %(fail_num/count_num*100)
        user_list = ['864652310@qq.com']
        sub = '接口自动化测试报告'
        content = "此次一共运行接口个数为%s个，通过个数%s个，失败个数%s个，通过率为%s" %(count_num,pass_num,fail_num,pass_result)
        self.send_mail(user_list,sub,content)

if __name__ == '__main__':
    sen = SendEmail()
    pass_list = [1,2,3,4,5]
    fail_list = [2,3,4,5,6,7]
    sen.send_main(pass_list,fail_list)

