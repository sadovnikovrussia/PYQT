class MyClass:
    def __init__(self, у):
        self.x = у

    def __hash__(self):
        return hash(self.x)


c = MyClass(10)
d = {}
d[c] = "Значение"
print(d[c])  # Выведет: Значение
