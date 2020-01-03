class Unit:
    ALL_UNIT_LIST = []
    def __init__(self, name):
        self.name = name
        Unit.ALL_UNIT_LIST.append(self)

Alice = Unit("Alice")
Becky = Unit("Becky")
# # print(Unit.ALL_UNIT_LIST[1].name)

# list = Unit.ALL_UNIT_LIST
# list[0].name = "changed"

# print(Unit.ALL_UNIT_LIST[0].name)

print(Unit.ALL_UNIT_LIST)

# print(id(Unit.ALL_UNIT_LIST))
# print(id(Alice.ALL_UNIT_LIST))
# print(id(Becky.ALL_UNIT_LIST))

print(id(Alice.name))
print(id(Becky.name))
print(id(Unit.name))