def deco(f):  # Функция-декоратор
    print("Bьrзвaнa функция func()")
    return f  # Возвращаем ссьmку на функцию


@deco
def func(x, y):
    return x + y


print(func(4, 5))