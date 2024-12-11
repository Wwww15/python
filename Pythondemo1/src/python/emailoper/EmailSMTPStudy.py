import smtplib
from email.mime.text import MIMEText


def send_txt_email(form_user, pwd, to_user, msg):
    mime_msg = MIMEText(msg, "plain", "utf-8")
    mime_msg.add_header("From",form_user)
    mime_msg.add_header("To",to_user)
    mime_msg.add_header("To","2338620561@qq.com")
    mime_msg.add_header("Subject","python测试")
    smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp_server.set_debuglevel(1)
    smtp_server.login(form_user, pwd)
    smtp_server.sendmail(form_user, [to_user,"2338620561@qq.com"], mime_msg.as_string())
    smtp_server.quit()


if __name__ == "__main__":
    from_user = "1006380802@qq.com"
    pwd = "bylogoytpvikbcgg"
    to_user = "1006380802@qq.com"
    send_txt_email(from_user,pwd,to_user,"你好，我是python初学者！")
