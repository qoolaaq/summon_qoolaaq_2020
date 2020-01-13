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
    def get_unit_information(unit):
        """
        引数はunit
            unit_name: 名前
            unit_color: カラー
            unit_team: チーム
            unit_position_type, unit_position_number: 場所
            unit_skill_information: スキルの内容
        を表示する
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
        return [
            unit_name,
            unit_color,
            unit_team,
            unit_position_type,
            unit_position_number,
            unit_skill_information
        ]
    def get_unit_information_panel_rect_list():
        return UnitInformationPanel.RECT_LIST

Alice = Unit("Alice", "FRIEND")
# print(UnitInformationPanel.get_unit_information_panel_rect_list())