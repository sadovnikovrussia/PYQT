class Class1:  # Базовьm класс для класса Class2

    def func1(self):
        print("Метод func1 () класса Classl")


class Class2(Class1):  # Класс Class2 наследует класс Classl
    def func2(self):
        print("Метод func2 () класса Class2")


class ClassЗ(Class1):  # Класс ClassЗ наследует класс Classl
    def func1(self):
        print("Meтoд func1 () класса ClassЗ")

    def func2(self):
        print("Meтoд func2 () класса ClassЗ")

    def funcЗ(self):
        print("Метод funcЗ () класса ClassЗ")

    def func4(self):
        print("Метод func4 () класса ClassЗ")


class Class4(Class2, ClassЗ):  # Множественное наследование
    def func2(self):
        ClassЗ.func2(self)

    def func4(self):
        print("Метод func4 () класса Class4")


с = Class4()  # Создаем экземnляр класса Class4
с.func1()  # Выведет: Метод funcl 1) класса ClassЗ
с.func2()  # Выведет: Метод func2 1) класса Class2
с.funcЗ()  # Выведет: Метод funcЗ 1) класса ClassЗ
с.func4()  # Выведет: Метод func4 1) класса Class4
setattr(Class4, "attr1", 10)
print(Class4.attr1)
print(Class4.__name__)
for i in Class4.__dict__:
    print(i)
print(Class1.__bases__)
print(str.__bases__)
