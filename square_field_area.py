# coding: utf-8

# from unit import *

"""
---positionについて---
ユニットの位置は、position_list[position_typeとposition_number]でデータを持っておく
position_list: [position_type, position_number]
position_type:フィールド、ベンチ(デッキ)、アウトサイド(セメタリ)
position_type: "field", "bench", "outside"
position_number: int(0~24)
基本的に位置情報はすべて上記のデータ構造で管理
フィールドの描写や、スキルの記述などは二次元リストで管理する…?

---Field, Area, Squareについて---
Field, AreaはSquareで構成される
ユニットの位置情報はすべてUnitをまとめたリストの方で管理する
Field, Area, Squareはそのリストから情報を引っ張ってくる
描写はFieldから情報を引っ張ってくる
スコアの計算等は、FieldやAreaから情報を引っ張ってくる

Square:
持つべき情報は、
そのスクエアがどこにあるのか
ユニットがいるのか否か、なんのユニットがいるか
どんなエフェクトがかかっているのか

Field:
持つべき情報は、
スクエアがそれぞれどこにいるのか(リストで持つ)
というか単なるリスト構造でいい気がする

Area:
持つべき情報は、
そのエリアにはどのスクエアが含まれるのか(リストで持つ)
というか単なるリスト構造でいい気がする
"""

class Square():
    # 位置情報、ユニットの有無、エフェクトを管理
    def __init__(self, coordinate):
        # 位置情報を受け取って、二次元リストでデータを持っておく
        # coordinate = [xpos, ypos], [ypos][xpos]となる
        self.coordinate = coordinate
        self.xpos = coordinate[0]
        self.ypos = coordinate[1]
        # coordinateをposition_numberに変換しておく
        self.position_number = self.xpos + 5*self.ypos
        # ユニットがいるかどうかを真偽値で管理
        # self.unit_exist = True or False
        self.unit_exist = False
        # エフェクトをリストで管理しておく
        self.effect_list = []
        # test用
        self._test_string = "I'm for test"
    """    
    def unit_exist_checker(self):
        # あんまり良くない書き方なので、思いつき次第書き直す
        # all_unit_listから、unit.position_listの情報を引っ張ってきて、評価
        print("test")
        self.unit_exist = False
        for unit in all_unit_list:
            if self.position_number == unit.position_number:
                self.unit_exist = True
    """
    def unit_exist_checker(self):
        self.unit_exist = False
        for unit in all_unit_list:
            if self.position_number == unit.position_number:
                self.unit_exist = True

class Field():
    def __init__(self):
        # このあたり事故る可能性ある
        # coordinate = [xpos, ypos], [ypos][xpos]となる
        self.list = [[Square([i,j]) for i in range(5)] for j in range(5)]

# フィールドを作成する
field = Field()

class Area():
    # 引数はdata_list
    # data_list[name, coordinate]
    def __init__(self, data_list):
        self.name = data_list[0]
        self.central_coordinate = data_list[1]
        # ここでfieldオブジェクトがあることを前提にしている。
        # まずい。
        self.list = [[field.list[data_list[1][0]+i][data_list[1][1]+j] for i in range(-1,2)] for j in range(-1,2)]
        # central_area.list[1][1].coordinate みたいな

# {name:[name, coordinate], ... }でデータを持つ
area_dictionary = \
     {"central_area":["central_area", [2,2]], \
         "right_upper_area":["right_upper_area", [3,1]], \
             "left_upper_area":["left_upper_area", [1,1]], \
                 "left_lower_area":["left_lower_area", [1,3]], \
                     "right_lower_area":["right_lower_area", [3,3]]}

def AreaInformationListGetter(keys):
    data_list = area_dictionary[keys]
    return data_list

# 各エリアを作成する
central_area = Area(AreaInformationListGetter("central_area"))
right_upper_area = Area(AreaInformationListGetter("right_upper_area"))
left_upper_area = Area(AreaInformationListGetter("left_upper_area"))
left_lower_area = Area(AreaInformationListGetter("left_lower_area"))
right_lower_area = Area(AreaInformationListGetter("right_lower_area"))

"""
print(central_area.list[1][1]._test_string)
central_area.list[1][1]._test_string = "I'm changed"
print(central_area.list[1][1]._test_string)
print(field.list[2][2]._test_string)
"""
