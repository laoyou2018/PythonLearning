# 面向过程
user1 = {'name': 'tom', 'hp': 100}
user2 = {'name': 'jerry', 'hp': 80}


def print_role(rolename):
    print('name is %s,hp is %s' % (rolename['name'], rolename['hp']))


print_role(user1)


# 面向对象
class Player():  # 定义一个类
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp # 两个下划线 修饰属性不能被实例访问 ：类的封装

    def print_role(self):
        print('name is %s,hp is %s' % (self.name, self.hp))


class Monster():
    '定义怪物类'
    pass # 没有定义实际内容的时候防止报错可以西安写个pass


user3 = Player('name', 100)
user3.print_role()
