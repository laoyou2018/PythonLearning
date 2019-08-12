chinese_zodiac_string = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# 用户输入
year = int(input('请输入出生年分'))

if chinese_zodiac_string[year % 12] == '狗':
    print('狗年运势记好')

# 打印今年是什么年份
print(chinese_zodiac_string[year % 12])
# for
for cz in chinese_zodiac_string:
    print(cz)

for i in range(12):
    print(i)

for year in range(2000, 2019):
    print('%s 年的生肖是%s' %(year, chinese_zodiac_string[year % 12]))

# while
a = 0
while True:
    print("a")
    a = a + 1

    if a > 10:
        break

# continue 继续下轮循环