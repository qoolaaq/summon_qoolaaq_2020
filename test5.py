def friend_starting_menber_list_get():
    return [
        "Alice", 
        "Becky", 
        "Cathy",
        "Daisy",
        "Emilia",
        "Flora",
        "Grace"
        ]
def enemy_starting_menber_list_get():
    return [
        "Reina",
        "Selena",
        "Tina",
        "Vivian",
        "Willow",
        "Yvonne",
        "Zara"
    ]

def skill_make(name):
    print(
        "def skill_of_{}".format(name) + "():"
        )
    print(
    #    "   "+'print("hello, I am {}")'.format(name)
    "    pass"
        )

def dictionary_make(name, color):
    # "Alice" : ["Alice", "Red", skill_of_Alice],
    print(
        '"{}"'.format(name), ":", '["{}",'.format(name), '"{}",'.format(color), 'skill_of_{}],'.format(name)
    )

# for name in enemy_starting_menber_list_get():
#     skill_make(name)

for name in friend_starting_menber_list_get():
    dictionary_make(name, "Red")
