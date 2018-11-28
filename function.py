## 函数相关

def test1(arg1):
    print(arg1)


def test2(arg1, arg2='hello'):
    print(arg1, arg2)


def test3(*args):
    print(args)


def test4(**kwargs):
    print(kwargs)


test1(12334)
test2('hexo')
test3(11, 22, 33)
test4(a = 'name', b = 'age')