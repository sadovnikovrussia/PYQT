class Class1: х = 10
class Class2(Class1): pass
class Class3(Class2): pass

class Class4(Class3): pass
class Class5(Class2): pass
class Class6(Class5): pass
class Class7(Class4, Class6): pass
с = Class7()
print(с.х)
print(Class7.__mro__)