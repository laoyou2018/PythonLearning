import time
print(time.time())
time.sleep(3)

# 装饰器

def i_can_sleep():
    time.sleep(3)


start_time = time.time()

i_can_sleep()

stop_time = time.time()

print('程序运行了 %s 秒' %(start_time - stop_time))

# 使用了装饰器
# 闭包传递是个变量 装饰器传递的是个函数
# 调用顺序是 在调用函数的时候 会先执行装饰器函数然后吧 函数作为参数传递给装饰器函数。

def timer(func):
    def warpper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('程序运行了 %s 秒' % (start_time - stop_time))
    return  warpper

@timer
def i_can_sleep1():
    time.sleep(3)

i_can_sleep1()


# 带参数的函数的 装饰器

def tips(fun):
    def nei(a,b):
        print('start')
        fun(a,b)
        print('end')
    return  nei

@tips
def add(a,b):
    print(a + b)

@tips
def sub(a,b):
    print(a - b)

add(3,5)
sub(6,7)

#  装饰器添加参数
def newtips(arg):
    def tips(fun):
        def nei(a, b):
            print('start %s %s' %(arg,fun.__name__))
            fun(a, b)
            print('end')

        return nei
    return tips

@newtips('add')
def add1(a,b):
    print(a + b)

@newtips('sub')
def sub1(a,b):
    print(a - b)


add1(3,5)
sub1(6,7)