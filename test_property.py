class Parent:
    def __init__(self, name):
        self.child = None
        self.name = name
    def get_child(self, child):
        self.child = child

class Child:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name

Mom = Parent("Mom")
Alice = Child("Alice", Mom)
Mom.get_child(Alice)

print(Mom.child.parent.child.parent.child.parent.name)