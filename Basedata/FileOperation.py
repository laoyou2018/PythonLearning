# 文件内建函数和方法：
# open 打开文件
# read 输入
# readline 输入一行
# seek 文件内移动
# write 输出
# close 关闭文件

# 将小说的主要任务记录在文件中

file1 = open('name.txt', 'w')
file1.write('诸葛亮')
file1.close()

file2 = open('name.txt')
print(file2.read())
file2.close()

file3 = open('name.txt', 'a')
file3.write('liubei')
file3.close()

file4 = open('name.txt')
print(file4.readline())
file4.close()

# read(a) 读取a个字符  没有参数是读取全部的内容
# tell() 可以知道seek目前在第几行
# seek（a，b）偏移 a：相对位置 b：0 开始 的位置 1 当前位置 2 是结尾