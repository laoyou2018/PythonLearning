# 函数的可变长参数
# 参数前面加* 代表参数可变长

def howlong(first, *other):
     print(len(other) + 1)


howlong(1,2,3)


# 函数变量域
# 如果函数内部的变量 添加global修饰 代表全局变量 外面的变量也会被改变
var1 = 123

def func():
    global var1
    var1 = 456
    print(var1)

func()
print(var1)

# 能对列表进行迭代的函数 叫做函数的迭代

list1 = [1, 2, 3]
it = iter(list1)
print(next(it))

# 函数生成器
for i in range(10, 20, 1):
    print(i)

# 小数  yield:运行到当前位置他会进行记录当前位置
def frange(star, stop, step):
    x = star
    while x < stop:
        yield x
        x += step

for i in frange(10, 20, 0.5):
    print(i)