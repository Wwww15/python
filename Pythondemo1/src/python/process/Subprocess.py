import subprocess


def dns_lookup():
    result = subprocess.call(['nslookup', 'www.python.org'])
    print("Exit Code:", result)


def communicate_lookup():
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output)
    return_code = p.returncode
    print(return_code)


if __name__ == '__main__':
    # dns_lookup()
    communicate_lookup()
