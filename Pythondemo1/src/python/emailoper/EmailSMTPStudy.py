import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fileinput import filename


def comm_header(mime_msg: MIMEBase, from_user, to_user):
    mime_msg.add_header("From", from_user)
    mime_msg.add_header("To", to_user)


def send_txt_email(form_user, pwd, to_user, msg):
    mime_msg = MIMEText(msg, "plain", "utf-8")
    comm_header(mime_msg, from_user, to_user)
    mime_msg.add_header("To", "2338620561@qq.com")
    mime_msg.add_header("Subject", "python测试")
    smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp_server.set_debuglevel(1)
    smtp_server.login(form_user, pwd)
    smtp_server.sendmail(form_user, [to_user, "2338620561@qq.com"], mime_msg.as_string())
    smtp_server.quit()


def send_html_email(form_user, pwd, to_user, msg):
    mime_msg = MIMEText(msg, "html", "utf-8")
    comm_header(mime_msg, from_user, to_user)
    mime_msg.add_header("Subject", "python测试html")
    mime_msg.add_header("To", "2338620561@qq.com")
    smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp_server.set_debuglevel(1)
    smtp_server.login(form_user, pwd)
    smtp_server.sendmail(from_user, [to_user, "2338620561@qq.com"], mime_msg.as_string())
    smtp_server.quit()


def send_attachment_email(from_user, pwd, to_user, file_path):
    # 邮件本身
    mime_msg = MIMEMultipart()
    comm_header(mime_msg, from_user, to_user)
    mime_msg.add_header("Subject", "python测试附件")
    mime_msg.add_header("To", "2338620561@qq.com")

    # 文本描述
    mime_text = MIMEText("你喜欢这个男孩吗", "plain", "utf-8")
    mime_msg.attach(mime_text)

    # 附件

    mime_base = MIMEBase("image", "jpg", filename="courage_boy.jpg")
    mime_base.add_header('Content-Disposition', 'attachment', filename='courage_boy.jpg')
    mime_base.add_header('Content-ID', '<0>')
    mime_base.add_header('X-Attachment-Id', '0')

    with open(file_path, 'rb') as f:
        mime_base.set_payload(f.read())

    encoders.encode_base64(mime_base)

    mime_msg.attach(mime_base)

    smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp_server.set_debuglevel(1)
    smtp_server.login(from_user, pwd)
    smtp_server.sendmail(from_user, [to_user, "2338620561@qq.com"], mime_msg.as_string())
    smtp_server.quit()


def send_img_email(from_user, pwd, to_user, msg, file_path):
    # 邮件本身
    mime_msg = MIMEMultipart()
    comm_header(mime_msg, from_user, to_user)
    mime_msg.add_header("Subject", "python测试图片")
    mime_msg.add_header("To", "2338620561@qq.com")

    # 附件
    mime_base = MIMEBase("image", "jpg", filename="courage_boy.jpg")
    mime_base.add_header('Content-Disposition', 'attachment', filename='courage_boy.jpg')
    mime_base.add_header('Content-ID', '<0>')
    mime_base.add_header('X-Attachment-Id', '0')

    with open(file_path, 'rb') as f:
        mime_base.set_payload(f.read())

    encoders.encode_base64(mime_base)

    mime_msg.attach(mime_base)

    # 图片
    mime_text = MIMEText(msg, "html", "utf-8")
    mime_msg.attach(mime_text)

    smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp_server.set_debuglevel(1)
    smtp_server.login(from_user, pwd)
    smtp_server.sendmail(from_user, [to_user, "2338620561@qq.com"], mime_msg.as_string())
    smtp_server.quit()


def send_html_and_txt_email(from_user, pwd, to_user, txt_msg, html_msg):
    mime_msg = MIMEMultipart("alternative")
    comm_header(mime_msg, from_user, to_user)
    mime_msg.add_header("Subject", "python测试html和文本")
    mime_msg.add_header("To", "2338620561@qq.com")

    mime_text = MIMEText(txt_msg, "plain", 'utf-8')
    mime_html = MIMEText(html_msg, "html", "utf-8")
    mime_msg.attach(mime_text)
    mime_msg.attach(mime_html)

    smtp_server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp_server.set_debuglevel(1)
    smtp_server.login(from_user, pwd)
    smtp_server.sendmail(from_user, [to_user, "2338620561@qq.com"], mime_msg.as_string())
    smtp_server.quit()


if __name__ == "__main__":
    from_user = "1006380802@qq.com"
    pwd = "bylogoytpvikbcgg"
    to_user = "1006380802@qq.com"
    # send_txt_email(from_user,pwd,to_user,"你好，我是python初学者！")

    # html_content = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
    # send_html_email(from_user, pwd, to_user, html_content)

    # file_path = "courage_boy.jpg"
    # send_attachment_email(from_user, pwd, to_user, file_path)

    # img_html = '<html><body><h1>Hello</h1><p>Do you like this boy ↓ <br/><img src="cid:0"></a></p></body></html>'
    # file_path = "courage_boy.jpg"
    # send_img_email(from_user, pwd, to_user, img_html, file_path)

    txt_content = "你好，我是python初学者！"
    html_content = '<html><body><h1>Hello</h1><p>Welcome to <a href="http://www.python.org">Python</a>...</p></body></html>'
    send_html_and_txt_email(from_user,pwd,to_user,txt_content,html_content)

