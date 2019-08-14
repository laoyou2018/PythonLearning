# 异常处理
print('异常处理')

# 为定义
# 语法错位
# 索引越界
# 字典的key错误
# 类型错误

try:
    year = int(input('input your name:'))
    a = open('name.txt')
except Exception as e:
    print('handle the exception %s' %e)
finally:
    # 关闭文件 这里是必然执行的
    a.close()