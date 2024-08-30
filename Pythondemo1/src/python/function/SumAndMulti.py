def sumAndMulti(val1,val2):
    if not isinstance(val1,(int,float)) and not isinstance(val1,(int,float)):
        raise TypeError('类型不对，参数类型为 int 和 float')

    a = val1 + val2;
    b = val1 * val2;
    return a,b
