class myClass:
    @staticmethod
    def func1(x, y):
        return x + y

    def func2(self, x, y):
        return x + y

    def func3(self, x, y):
        return myClass.func1(x, y)


print(myClass.func1(10, 20))
c = myClass()
print(c.func2(5, 10))
print(c.func1(50, 12))
print(c.func3(23, 5))