# filter()
# map()
# reduce()
# zip()

# 以上是内建函数

# 闭包

def func():
    num1 = 1
    num2 = 2
    print(num1 + num2)

# 内部函数引用了外部函数的变量
def sum(a):
    def add(b):
        return  a + b
    return  add

num1 = func()

num2 = sum(2)
print(num2(3))

print(type(num1))
print(type(num2))

# 闭包实现计数器
def counter():
    cnt = [0]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return  add_one

num3 = counter()
print(num3())
print(num3())
print(num3())
print(num3())

# 闭包的应用
# a*x + b = y

def a_line(a, b):
    def arg_y(x):
        return a*x + b
    return  arg_y
# lambda 表达式简化
def a_line1(a, b):
    return  lambda x:a*x + b

line1 = a_line(3,5)
print(line1(10))
print(line1(20))

line2 = a_line1(3,5)
print(line2(10))
print(line2(20))