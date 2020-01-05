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
        # coordinate = [xpos, ypos]
        # Fieldオブジェクトでは、FIELD[ypos][xpos]となる
        self.coordinate = coordinate
        self.xpos = coordinate[0]
        self.ypos = coordinate[1]
        # coordinateをposition_numberに変換しておく
        self.position_number = self.xpos + 5*self.ypos
        # ユニットオブジェクトを直接代入して持っておく
        # 初期値はNoneにしておく
        self.unit = None
        # ユニットがいるかどうかを真偽値で管理
        # self.unit_exist = True or False
        self.unit_exist = False
        # エフェクトをリストで管理しておく
        self.effect_list = []
        # # test用
        # self._test_string = "I'm for test"
        self.type = "square"
        # unitオブジェクトのタイプをこっから引っ張ってくる
        self.position_list = [self.type, self.position_number]
        # position_listを各自持っておく

    def unit_exist_reset(self):
        # unit_existの値を更新する
        # unitがそのスクエアにいれば、True、いなければFalse
        self.unit_exist = False
        if self.unit == None:
            pass
        else:
            self.unit_exist = True

    def unit_delete(self):
        # unitをNoneにする
        # unit_existはFalseにする
        self.unit_exist = False
        self.unit = None

    def unit_place(self,unit):
        # 引数としてunitオブジェクトをとる
        # unitに引数を入れる
        # unit_existをTrueにする
        self.unit = unit
        self.unit_exist = True

    def add_effect(self, effect):
        self.effect_list.append(effect)

    def unit_placable_get(self):
        return self.unit_exist

    def type_get(self):
        return self.type

    def position_list_get(self):
        """
        squareのposition_listを返す
        """
        return self.position_list

class Field(list):
    # 5*5の2次元リストオブジェクトを作成する
    # 各要素はすべてsquareオブジェクトとなっている
    def __init__(self):
        for row in Field.__field_make():
            self.append(row)
        # 割と強引に作った
        # field_maker()の返り値が作りたいオブジェクトそのものなのだが、
        # self = Field.field_maker()と出来なかったので、一度バラして突っ込んだ。
    def __field_make():
        # このあたり事故る可能性ある
        # coordinate = [xpos, ypos], [ypos][xpos]となる
        return [[Square([i,j]) for i in range(5)] for j in range(5)]

class Area(list):
    # 引数はFIELDオブジェクト、data_list
    # data_list[name, coordinate]
    global Field
    def __init__(self, FIELD, area_name):
        data_list = Area.__area_information_list_get(area_name)
        # data_list = [名前, 中央のsquareの座標]
        self.name = data_list[0]
        self.central_coordinate = data_list[1]
        # ここでFIELDオブジェクトがあることを前提にしている。
        # まずい。
        for row in Area.__area_make(self, FIELD, data_list):
            self.append(row)
        # 割と強引に作った
        # area_maker()の返り値が作りたいオブジェクトそのものなのだが、
        # self = Area.area_maker()と出来なかったので、一度バラして突っ込んだ。
        # central_area.list[1][1].coordinate みたいな
    def __area_make(self, FIELD, data_list):
        return [[FIELD[data_list[1][0]+i][data_list[1][1]+j] for i in range(-1,2)] for j in range(-1,2)]
        # 割と強引に作った
    def __area_information_list_get(keys):
        data_list = area_dictionary[keys]
        return data_list

# {name:[name, coordinate], ... }でデータを持つ
area_dictionary = \
     {"central_area":["central_area", [2,2]], \
         "right_upper_area":["right_upper_area", [3,1]], \
             "left_upper_area":["left_upper_area", [1,1]], \
                 "left_lower_area":["left_lower_area", [1,3]], \
                     "right_lower_area":["right_lower_area", [3,3]]}

"""
# mainに移した

FIELD = Field()

# 各エリアを作成する
CENTRAL_AREA = Area(FIELD, "central_area")
RIGHT_UPPER_AREA = Area(FIELD, "right_upper_area")
LEFT_UPPER_AREA = Area(FIELD, "left_upper_area")
LEFT_LOWER_AREA = Area(FIELD, "left_lower_area")
RIGHT_LOWER_AREA = Area(FIELD, "right_lower_area")
# 全てのエリアを統括するリストを作成する
ALL_AREA_LIST = [CENTRAL_AREA, RIGHT_UPPER_AREA, LEFT_LOWER_AREA, \
    RIGHT_UPPER_AREA]
"""