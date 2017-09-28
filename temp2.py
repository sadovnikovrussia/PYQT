class Class1:  # Базовый класс
    def __init__(self):
        print("Конструктор базового класса")

    def func1(self):
        print("Метод func1 () класса Class1")


class Class2(Class1):   # Класс Class2 наследует класс Class1

    def __init__(self):
        print("Конструктор nроизводного класса")
        Class1.__init__(self)  # Вызываем конструктор базового класса

    def func1(self):
        print("Метод func1 () класса Class2")
        Class1.func1(self)  # Вызываем метод базового класса


с = Class2()
с.func1()
# Создаем экземnляр класса Class2
# Вызываем метод funcl ()
