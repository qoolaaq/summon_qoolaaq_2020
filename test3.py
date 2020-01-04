class Unit:
    ALL_UNIT_LIST = []
    def __init__(self, name):
        self.name = name
        Unit.ALL_UNIT_LIST.append(self)

class AnotherUnit:
    ANOTHER_UNIT_LIST = []
    def __init__(self,name):
        self.name = name
        AnotherUnit.ANOTHER_UNIT_LIST.append(self)

Alice = Unit("Alice")
# Becky = Unit("Becky")
Cashy = AnotherUnit("Cashy")

Alice.name = Cashy.name
print("###Alice.name is Cashy.name")
print("Alice.name is", Alice.name)
print("Alice.name id is", id(Alice.name))
print("Cashy.name id is", id(Cashy.name))
print("Cashy.name is", Cashy.name)


"""
Alice = Unit("Alice")
# Becky = Unit("Becky")
# Cashy = AnotherUnit("Cashy")

print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)

name = Alice.name
print("###name is Alice.name")
print("name is", name)
print("name id is", id(name))
print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)

name = "another Alice"
print("###name is another Alice")
print("name is", name)
print("name id is", id(name))
print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)

del Alice.name
print("###del Alice.name")
print("name is", name)
print("name id is", id(name))
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)

Alice.name = name
print("###Alice.name is name")
print("name is", name)
print("name id is", id(name))
print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)

del name
print("###del name")
# print("name is", name)
# print("name id is", id(name))
print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)
"""
