def absFun(val):
    if not isinstance(val,(int,float)):
        raise TypeError('传入参数类错误，需要 int 和 float')
    if val > 0:
        return val
    else:
        return -val
