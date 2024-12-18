import poplib
from email.header import decode_header
from email.message import Message
from email.parser import Parser
from email.utils import parseaddr


def get_email(user, pwd, addr, port):
    pop_server = poplib.POP3_SSL(addr, port)
    pop_server.set_debuglevel(1)
    welcome_msg = pop_server.getwelcome().decode("utf-8")
    print(welcome_msg)
    pop_server.user(user)
    pop_server.pass_(pwd)
    # 获取邮件统计展示信息
    msg_num, size = pop_server.stat()
    print("Messges: %s ,Size: %s" % (msg_num, size))

    # 获取响应和邮件列表
    resp, mails, octets = pop_server.list()
    print("resp: %s" % resp)
    print("mails: %s" % mails)
    print("octets: %s" % octets)

    # 获取最近一封邮件
    resp, mail, octets = pop_server.retr(len(mails))
    index = len(mails)
    print("resp: %s" % resp)
    print("mail: %s" % mail)
    print("octets: %s" % octets)
    print("mails size: %s" % index)

    # 解析展示邮件本身
    decode_msg = b'\r\b'.join(mail).decode("utf-8")
    email_msg = Parser().parsestr(decode_msg)
    print(email_msg)

    pop_server.quit()
    return  email_msg


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get("Content-Type", "").lower()
        pos = content_type.find("charset=")
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    for header in ["From", "To", "Subject"]:
        value = msg.get(header, "")
        if value:
            if header == "Subject":
                value = decode_str(value)
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = "%s <%s>" % (name, addr)
        print("%s%s: %s" % ("  " * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print("%spart %s" % ("  " * indent, n))
            print("%s--------------------" % ("  " * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print("%sText: %s" % ("  " * indent, content + b''))
        else:
            print("%sAttachment: %s" % ("  " * indent, content_type))


if __name__ == "__main__":
    user = "1006380802@qq.com"
    pwd = "irwmidkbtrmibfgj"
    addr = "pop.qq.com"
    port = 995

    email_msg = get_email(user, pwd, addr, port)
    print("\r\b")
    print_info(email_msg.get_payload())

