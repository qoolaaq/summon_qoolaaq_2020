# coding: utf-8

# ユニットすべてをリストとして管理する
all_unit_list = []

# ユニットごとにスキルを関数として定義しておく
# スキルをユニットごとに定義するの大変だけど仕方ない
# 要改良
def skill_of_Alice():
    print("hello, I'm Alice")

def skill_of_Becky():
    print("hello, I'm Becky")

# ユニットの名前、パワー、カラーの辞書型データ
# 名前：［名前、パワー、カラー, スキル］
unit_dictionary = \
    {"Alice" : ["Alice", 15, "Red", skill_of_Alice], \
        "Becky" : ["Becky", 12, "Red", skill_of_Becky]}


# 名前を引数として受け取って、UnitDictionaryからリストとして情報を引っ張ってくる
# name → datalist = [name, power, color, skill]
def UnitInformationListGetter(keys):
    data_list = unit_dictionary[keys]
    return data_list

# 引数として名前とチームを受け取って、ユニットオブジェクトを作成する
class Unit():
    # datalist: UnitInformationGetterで引っ張ってくるリスト
    # team: 文字列、敵か味方か
    # position_list: [position_type, position_number]
    # position_type: "field", "bench", "outside"
    # position_number: int(0~24)
    def __init__(self, data_list, team, position_list):
        # UnitInformationGetterでプロパティを定義する。
        self.name = UnitInformationListGetter(data_list)[0]
        self.power = UnitInformationListGetter(data_list)[1]
        self.color = UnitInformationListGetter(data_list)[2]
        self.skill = UnitInformationListGetter(data_list)[3]

        # teamをプロパティとして紐付ける
        self.team = team
        # 位置情報をプロパティとして紐付ける
        self.position_list = position_list
        self.position_type = self.position_list[0]
        self.position_number = self.position_list[1]

        """
        # selfをall_unit_listを入れる
        all_unit_list.append(self)
        """
