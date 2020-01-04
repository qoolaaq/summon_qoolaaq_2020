class Unit:
    ALL_UNIT_LIST = []
    def __init__(self, name, test):
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



# name = Cashy.name
# print("##########name is Cashy##########")
# print("name id is", id(name))
# print("name is", name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# Cashy.name = Cashy.name + "Another"
# print("##########Cashy.name is CashyAnother##########")
# print("name id is", id(name))
# print("name is", name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# print("##########Alice is not Cashy")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# Alice = Cashy
# print("##########Alice is Cashy##########")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# Alice.name = Cashy.name
# print("##########Alice.name is Cashy.name##########")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# Alice.name = "another Alice"
# print("##########Alice.name is another Alice")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# Alice.name = Alice.name + "Another"
# print("##########Alice.name is AliceAnother")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# Cashy.name = Cashy.name + "Another"
# print("##########Cashy.name is CashyAnother##########")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# del Alice
# print("##########del Alice")
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

# del Cashy
# print("##########del Cashy")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)

# del Cashy.name
# print("##########del Cashy.name")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Alice.name id is", id(Alice.name))
# print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# # print("Cashy.name id is", id(Cashy.name))
# # print("Cashy.name is", Cashy.name)

# del Alice.name
# print("##########del Alice.name")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# # print("Alice.name id is", id(Alice.name))
# # print("Alice.name is", Alice.name)
# print("Cashy id is", id(Cashy))
# print("Cashy is", Cashy)
# print("Cashy.name id is", id(Cashy.name))
# print("Cashy.name is", Cashy.name)

"""
Alice.name = Cashy.name
print("###Alice.name is Cashy.name")
print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)
print("Cashy.name id is", id(Cashy.name))
print("Cashy.name is", Cashy.name)

del Alice.name
print("###del Alice.name")
print("Cashy.name id is", id(Cashy.name))
print("Cashy.name is", Cashy.name)

del Cashy.name
print("###del Cashy.name")
print("Alice.name id is", id(Alice.name))
print("Alice.name is", Alice.name)
"""

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
