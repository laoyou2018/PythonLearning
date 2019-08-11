# 星座
zodiac_name = ('魔蝎座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
               '狮子座', '处女座', '天平座', '天蝎座', '射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
               (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# 元祖的比较
print((4) > (5))
# 这里的元祖可以看作是 421 和 520  标记大小
print((4, 21) > (5, 20))


(month, day) = (2, 15)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_len)
print(zodiac_name[zodiac_len])

# 列表和元祖
# 区别是可以修改数据 元祖不可以
a_list = ['abc', 'zxc']
a_list.append('X')
print(a_list)
a_list.remove('abc')
print(a_list)

# 和字符串的操作基本相同