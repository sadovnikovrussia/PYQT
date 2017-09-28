class chislo:
    def __init__(self, y):
        self.x = y

    def __add__(self, other):
        print("экземпляр слева")
        return other + self.x


ch = chislo(10)


def method_name():
    ch + 5 +


method_name()
print()