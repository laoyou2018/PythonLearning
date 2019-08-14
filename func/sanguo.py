# 读取人物名称

f = open('name.txt')
data = f.read()

print(data.split('|'))

# 读取兵器
f2 = open('weapon.txt')
data2 = f2.read()

i = 1
for line in f2.readlines():
    if i % 2 == 1:
        # 去掉后面的换行符
        print(line.strip('\n'))
    i += 1


# 中文编码
f3 = open('sanguo.txt', encoding='Gb18030')
print(f3.read().replace('\n', ''))


# 函数功能
def func(filename):
    try:
       f = open(filename)
    except Exception:
       print('error')

func('name')


# a  在dd中出现的次数 结果是集合列表
# import re
# re.findall("a",dd)