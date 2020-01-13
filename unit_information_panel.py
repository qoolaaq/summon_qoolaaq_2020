from unit import *
from unit_dictionary import *

class UnitInformationPanel:
    unit_dictionary = UnitDictionary.unit_dictionary
    WIDTH = 270
    HEIGHT = 120
    POSITION = (360, 220)
    RECT_LIST = (
        POSITION[0],
        POSITION[1],
        WIDTH,
        HEIGHT
    )
    # とりあえずハードコーディングしている
    # 左下の端が(630, 340)だったので、そこから幅と高さは計算した

    color_FRIEND = (255, 255, 255)
    # いないのはwhite
    color_ENEMY = (0, 0, 0)
    # いるのはblack
    def get_unit_information_letters(unit):
        """
        引数はunit
            unit_name: 名前
            unit_color: カラー
            unit_team: チーム
            unit_position_type, unit_position_number: 場所
            unit_skill_information: スキルの内容
        返り値はリスト =
            [上記の変数を上から順に]
        # 本当はpanelを受け取って情報を表示したい
        # うまい処理が見つかれば切り替える(2020/01/13)
        """
        unit_name = unit.name
        unit_color = unit.color
        unit_team = unit.team
        unit_position_type = unit.position_type
        unit_position_number = unit.position_number
        ###
        unit_skill_information = None
        ###
        # スキルの方に説明文を作って、それを表示するようにする
        
        # return [
        #     unit_name,
        #     unit_color,
        #     unit_team,
        #     unit_position_type,
        #     unit_position_number,
        #     unit_skill_information
        # ]

        # letters = \
        #     "name:" + unit_name + "\n" \
        #         + "team:" + unit_team + "\n"\
        #             + "color:" + unit_color + "\n"\
        #                 + "position:" + unit_position_type \
        #                     + str(unit_position_number) + "\n"
        # letters = \
        #     """
        #     name:{}
        #     team:{}
        #     color:{}
        #     position:{}{}
        #     """.format(
        #         unit_name,
        #         unit_team,
        #         unit_color,
        #         unit_position_type,
        #         str(unit_position_number)
        #         )
        return unit_name
        # 改行が上手く行かなかったので、とりあえずunit_nameを返している。
    def get_unit_information_panel_rect_list():
        """
        RECT_LISTを返す
        # WIDTH = 270
        # HEIGHT = 120
        # POSITION = (360, 220)
            RECT_LIST = (
                POSITION[0], :360
                POSITION[1], :220
                WIDTH,       :270
                HEIGHT       :120
            )
        # とりあえずハードコーディングしている
        # 左下の端が(630, 340)だったので、そこから幅と高さは計算した        
        """
        return UnitInformationPanel.RECT_LIST
    def get_unit_information_panel_letter_color(unit):
        """
        unitを引数として、色を返す
        unitがいなければNoneを返す
        """
        if unit.team == "FRIEND":
            return UnitInformationPanel.color_FRIEND
        elif unit.team == "ENEMY":
            return UnitInformationPanel.color_ENEMY
        else:
            return None


# Alice = Unit("Alice", "FRIEND")
# Alice.position_type = "test"
# Alice.position_number = 1
# print(UnitInformationPanel.get_unit_information_letters(Alice))