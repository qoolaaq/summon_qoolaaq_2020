unit_name_list = [
        "Alice",
        "Becky",
        "Cathy",
        "Daisy",
        "Emilia",
        "Flora",
        "Grace",

        "Reina",
        "Selena",
        "Tina",
        "Vivian",
        "Willow",
        "Yvonne",
        "Zara"
    ]

# unit_name_listから、
#     class SkillOfName(Skill):
#         def __init__(self):
#             super().__init__()
        # def effect(
        #     self,
        #     ALL_UNIT_LIST,
        #     FIELD,
        #     ALL_AREA_LIST,
        #     ALL_BENCH_LIST,
        #     ALL_OUTSIDE_LIST,
        #     STARTING_MEMBER_LIST,
        #     SKILL_PROCESSOR
        #     ):
# をつくる
for name in unit_name_list:
    print(
        "class", "SkillOf{}(Skill):".format(name)
    )
    print("    def __init__(self):")
    print("        super().__init__()")
    print("""    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass""")
    print("")


# # unit_name_listから、
# #     skill_of_Name = SkillOfName()
# # をつくる
# for name in unit_name_list:
#     print(
#         "skill_of_{} = SkillOf{}()".format(name, name)
#     )