passw = input("Введите па роль: ")
passw = passw.rstrip("\r")
print(passw)


def test_passw(p):
    def deco(f1,f2):
        if p == "10":
            return f1
        #elif p == '9':
         #   return f2
        else:
            return lambda: "Доступ закрыт"

    return deco  # Возвращаем функцию-декоратор


@test_passw(passw)
def func():
    return print("Доступ открыт")


def func2():
    return print("Доступ приоткрыт")


func()  # Вызываем функцию
