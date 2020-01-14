from skill import *

class SkillProcessor():
    """
    skillを入れて、順次処理していく
    """
    def __init__(self):
        self.list = []
        pass
    def load_skill(self, skill):
        """
        スキルを解決するリストに載せておく
        """
        self.list.append(skill)
    def process_skill(self):
        """
        list内のスキルを順次使っていく
        """
        for skill in self.list:
            skill.effect()


"""
以下テスト
for 文を回している最中にスキルをロードさせても
ちゃんと処理することを確認
"""

SKILL_PROCESSOR = SkillProcessor()

class skill_for_test_A:
    def effect():
        print("i am A and processed")


def func_test():
    global skill_for_test_A
    global SKILL_PROCESSOR
    SKILL_PROCESSOR.load_skill(skill_for_test_A)

class skill_for_test_B:
    def effect():
        print("i am B and processed")
        func_test()



SKILL_PROCESSOR.load_skill(skill_for_test_A)
SKILL_PROCESSOR.load_skill(skill_for_test_B)
SKILL_PROCESSOR.process_skill()