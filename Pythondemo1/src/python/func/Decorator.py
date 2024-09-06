def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def hello():
    print('hello')


hello()


def log1(text):
    def decorate(func):
        def warp():
            print('%s call %s()' % (text, func.__name__))
            return func()

        return warp

    return decorate


@log1('zhangsan')
def sayHi():
    print('sayHi')


sayHi()
