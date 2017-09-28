class MyClass:
    def __init__(self, m):
        self.msg = m
        self.i = 'i'
        print("Инициировние,", 'аргумент =')

    def __call__(self):  # обращение как к функции
        print('обращение как к функции', self.msg)

    def __getitem__(self, item):
        return self.msg[item]

    def __setitem__(self, key, value):
        self.msg[key] = value

    def __getattr__(self, attr):
        print('Вызван метод __getattr__(),', 'метода', '.', attr,
              'не существует')

    def __getattribute__(self, attr2):
       print('вызван __getattribute__()')
       return object.__getattribute__(self, attr2)

    def __setattr__(self, attr3, value2):
       print('вызван метод __setattr__()')
       self.__dict__[attr3] = value2

# c1 = MyClass('arg1')  # Создание экземnляра класса
c2 = MyClass('аргумент')  # Создание экземnляра класса
# c1()  # обращени как к функции
c2()
# c = MyClass([1, 2, 3, 4, 5])
# print(c[0])
# for i in c: print(i, end=' ')
# print()
# print(list(c))
# print(c.r)  # несуществующий атриут
# print(c.i)
# c2.y = 'yy'
#print(c2.y)
#print(c2.__dict__)
#c2()
