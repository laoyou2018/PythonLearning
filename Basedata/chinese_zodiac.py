#  记录我们的十二生肖 根据年份来计算

chinese_zodiac = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']

chinese_zodiac_string = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

first = chinese_zodiac_string[0]  # 第一个元素
print(first)
# 从第零个开始 四个元素
print(chinese_zodiac_string[0:4])
# 最后一个元素
print(chinese_zodiac_string[-1]) 

year = 2018
# 打印今年是什么年份
print(chinese_zodiac_string[year % 2])


# 序列的基本操作
# 包含操作
c = '狗' in chinese_zodiac_string
print(c)
# 连接操作
print(chinese_zodiac_string + 'abc')
# 重复操作
print(chinese_zodiac_string * 3)
# 切片操作
print(chinese_zodiac_string[0:4])
