Alice = "Alice"
Becky = Alice
print("#####Becky is Alice#####")
print("Alice id is", id(Alice))
print("Becky id is", id(Becky))

# Alice = "AliceAnother"
# print("#####Alice is AliceAnother#####")
# print("Alice id is", id(Alice))
# print("Alice is", Alice)
# print("Becky id is", id(Becky))
# print("Becky is", Becky)

Becky = "AliceAnother"
print("#####Becky is AliceAnother#####")
print("Alice id is", id(Alice))
print("Alice is", Alice)
print("Becky id is", id(Becky))
print("Becky is", Becky)
