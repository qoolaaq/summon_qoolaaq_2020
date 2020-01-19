# coding: utf-8
from unit_dictionary import *

# 引数として名前とチームを受け取って、ユニットオブジェクトを作成する
class Unit():
    """
    # datalist: UnitInformationGetterで引っ張ってくるリスト
    # team: 文字列、敵か味方か(FRIENDかENEMYか)
    # position_list: [position_type, position_number]
    # position_type: "square", "bench", "outside"
    # "field"よりもsquareにした方が良さそうだったので変えた(20/01/05)
    # position_number: int(0~24)
    # position_typeとnumberは紐付いてないと意味ないので、リストで持つ
    # targetable: bool, 効果の対象になるかどうかを決める
    """
    def __init__(self, unit_name: str, team):
        # UnitInformationGetterでnameから情報を引っ張ってきてプロパティを定義する。
        # datalist = [name, color, skill]
        self.name = UnitDictionary.get_unit_information(unit_name)[0]
        self.color = UnitDictionary.get_unit_information(unit_name)[1]
        self.skill = UnitDictionary.get_unit_information(unit_name)[2]

        # teamをプロパティとして紐付ける
        self.team = team

        # 位置情報をプロパティとして紐付ける
        self.position_type = None
        self.position_number = None
        self.position_list = [self.position_type, self.position_number]

        # 効果の対象になるかどうか
        self.targetable = True

    def type_chnage(self, position_type):
        # 引数としてタイプを受け取る
        # 返り値はなし
        # 出来ればここで勝手にポジションが変わるようにしたい
        self.position_type = position_type
    
    def position_list_change(self, position_list):
        """
        # 引数としてposition_listを受け取る
        # 返り値はなし
        # 出来ればここで勝手にポジションが変わるようにしたい
        """
        self.position_type = position_list[0]
        self.position_number = position_list[1]
        self.position_list = position_list

    def position_number_return(self):
        """
        position_numberを返す
        """
        return self.position_number
    def is_targetable(self):
        """
        targetablae を返す
        """
        return self.targetable
    def chenge_targetable(self):
        """
        targetableをFalseにする
        """
        self.targetable = False