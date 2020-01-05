# coding: utf-8

# ユニットすべてをリストとして管理する
# グローバル変数としてmainで宣言することにした
# ALL_UNIT_LIST = []

# ユニットごとにスキルを関数として定義しておく
# スキルをユニットごとに定義するの大変だけど仕方ない
# 要改良
def skill_of_Alice():
    print("hello, I'm Alice")
def skill_of_Becky():
    print("hello, I'm Becky")
def skill_of_Cashy():
    print("hello, I'm Cashy")

# ユニットの名前、カラーの辞書型データ
# 名前：［名前、カラー, スキル］
# パワーは実装しないことにした
unit_dictionary = \
    {"Alice" : ["Alice", "Red", skill_of_Alice], \
        "Becky" : ["Becky", "Red", skill_of_Becky], \
            "Cashy" : ["Cashy", "Red", skill_of_Cashy]}

# 名前を引数として受け取って、UnitDictionaryからリストとして情報を引っ張ってくる
# name → datalist = [name, color, skill]
def unit_information_get(keys):
    data_list = unit_dictionary[keys]
    return data_list

# 引数として名前とチームを受け取って、ユニットオブジェクトを作成する
class Unit():
    # datalist: UnitInformationGetterで引っ張ってくるリスト
    # team: 文字列、敵か味方か
    # position_list: [position_type, position_number]
    # position_type: "square", "bench", "outside"
    # "field"よりもsquareにした方が良さそうだったので変えた(20/01/05)
    # position_number: int(0~24)
    # position_typeとnumberは紐付いてないと意味ないので、リストで持つ
    def __init__(self, unit_name: str, team):
        # UnitInformationGetterでnameから情報を引っ張ってきてプロパティを定義する。
        # datalist = [name, color, skill]
        self.name = unit_information_get(unit_name)[0]
        self.color = unit_information_get(unit_name)[1]
        self.skill = unit_information_get(unit_name)[2]

        # teamをプロパティとして紐付ける
        self.team = team

        # 位置情報をプロパティとして紐付ける
        self.position_type = None
        self.position_number = None
        self.position_list = [self.position_type, self.position_number]
    
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
