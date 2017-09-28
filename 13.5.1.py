class MyClass:
    def __init__(self, a):
        self.arr = a
        self.i = 'infa'
        print('инициализация')

    def __len__(self):
        return len(self.i)

    def prt(self):
        print(self.i)

p = 6
print(p)
c = MyClass(5)
c.prt()

print(len(c))
