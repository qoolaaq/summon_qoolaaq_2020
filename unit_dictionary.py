from skill_list import *

skill_of_Alice = SkillOfAlice()
skill_of_Becky = SkillOfBecky()
skill_of_Cathy = SkillOfCathy()
skill_of_Daisy = SkillOfDaisy()
skill_of_Emilia = SkillOfEmilia()
skill_of_Flora = SkillOfFlora()
skill_of_Grace = SkillOfGrace()
skill_of_Reina = SkillOfReina()
skill_of_Selena = SkillOfSelena()
skill_of_Tina = SkillOfTina()
skill_of_Vivian = SkillOfVivian()
skill_of_Willow = SkillOfWillow()
skill_of_Yvonne = SkillOfYvonne()
skill_of_Zara = SkillOfZara()

class UnitDictionary:
    """
    Unitのname, color, skillをリストとして管理する
    unit_dictionary = {"unit_name" : ["unit_name", "unit_color", unit_skill]}
    """
    unit_dictionary = {
        "Alice" : ["Alice", "Red", skill_of_Alice],
        "Becky" : ["Becky", "Red", skill_of_Becky],
        "Cathy" : ["Cathy", "Red", skill_of_Cathy],
        "Daisy" : ["Daisy", "Red", skill_of_Daisy],
        "Emilia" : ["Emilia", "Red", skill_of_Emilia],
        "Flora" : ["Flora", "Red", skill_of_Flora],
        "Grace" : ["Grace", "Red", skill_of_Grace],

        "Reina" : ["Reina", "Red", skill_of_Reina],
        "Selena" : ["Selena", "Red", skill_of_Selena],
        "Tina" : ["Tina", "Red", skill_of_Tina],
        "Vivian" : ["Vivian", "Red", skill_of_Vivian],
        "Willow" : ["Willow", "Red", skill_of_Willow],
        "Yvonne" : ["Yvonne", "Red", skill_of_Yvonne],
        "Zara" : ["Zara", "Red", skill_of_Zara]
    }

    def __init__(self):
        pass
    def get_unit_dictionary():
        """
        unit_dictionaryを返す
        """
        return UnitDictionary.unit_dictionary
    def get_unit_information(keys):
        """
        引数はkey
        返り値はlist = [unit_name, unit_color, unit_skill]
        """
        data_dictionary = UnitDictionary.get_unit_dictionary()
        data_list = data_dictionary[keys]
        return data_list

    # """
    # 以下、各ユニットのSkillをクラスメソッドとして持っておく
        # 色々とやってみたけど無理だった。
        # クラス内でクラスメソッドをリストやディクショナリに入れられなかった
    # """
    # def skill_of_Alice():
    #     print("hello. Alice")
    # def skill_of_Becky():
    #     UnitDictionary.skill_of_Alice()
    # def skill_of_Cathy():
    #     pass
    # def skill_of_Daisy():
    #     pass
    # def skill_of_Emilia():
    #     pass
    # def skill_of_Flora():
    #     pass
    # def skill_of_Grace():
    #     pass

    # def skill_of_Reina():
    #     pass
    # def skill_of_Selena():
    #     pass
    # def skill_of_Tina():
    #     pass
    # def skill_of_Vivian():
    #     pass
    # def skill_of_Willow():
    #     pass
    # def skill_of_Yvonne():
    #     pass
    # def skill_of_Zara():
    #     pass

