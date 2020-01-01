# coding: utf-8

class Square():
    def __init__(self,number):
        self.number = number
        self.unit = None
        self.unit_exist = False

    def unit_exist_reset(self):
        self.unit_exist = False
        if self.unit == None:
            pass
        else:
            self.unit_exist = True

    def unit_delete(self):
        self.unit_exist = False
        self.unit = None

    def unit_placed(self,unit):
        self.unit = unit
        self.unit_exist = True
        # print("I'm read")

class Unit():
    def __init__(self, name, number):
        self.name = name
        self.number = number

squareA = Square(0)
# print(squareA.number)

def UnitMaker(name, number):
    self = Unit(name, number)

    square = squareA
    square.unit_placed(self)

Alice = UnitMaker("Alice", 0)
print(squareA.unit.name)
