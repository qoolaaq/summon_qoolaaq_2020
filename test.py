# coding: utf-8

class Field(list):
    def __init__(self):
        self = self.append([[i+6*j for i in range(6)] for j in range(6)])
    pass

#field = Field()
#field.append([[i+6*j for i in range(6)] for j in range(6)])

a = Field()
print(a)
