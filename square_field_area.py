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
        """
        引数としてunitオブジェクトをとる
        square.unitに引数を入れる
        unit_existをTrueにする
        """
        self.unit = unit
        self.unit_exist = True

    def add_effect(self, effect):
        self.effect_list.append(effect)

    def unit_placable_get(self):
        """
        unit_exist: boolを返す
        """
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
    """
    # 各エリアは3✕3の9マスとなっている
    # すべてのエリアにおいて、各ユニットが何体いるのかを把握しておく
    """
    global Field
    def __init__(self, FIELD, area_name):
        """
        # 引数はFIELDオブジェクト、data_list = [name, coordinate]
        # self.name: 名前
        # self.central_coordinate: 中心の座標[xpos, ypos]
        # self.dictionary = {team_name : number_of_unit}
        # self.occupaied_team = "FRIEND" or "ENEMY" (最初はNone)
        """
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
        # CENTRAL_AREA.list[1][1].coordinate みたいな
        self.dictionary = {
            "FRIEND" : 0,
            "ENEMY": 0
            }
        self.occupaied_team = None
        # とりあえずFRIENDとENEMYのみしかチームがないという想定で書いてしまっている
    def __area_make(self, FIELD, data_list):
        central_coordinate = data_list[1]
        return [
            [FIELD[central_coordinate[1]+i][central_coordinate[0]+j] 
            for i in range(-1,2)] 
            for j in range(-1,2)
            ]
        # [ypos][xpos] = [ypos, ypos]
        # 割と強引に作った
    def __area_information_list_get(keys):
        data_list = area_dictionary[keys]
        return data_list
    def reset_area_dictionary(self):
        """
        # 各エリアにどのチームのユニットが何体いるのかをself.dictionaryに記録する
        # とりあえずFRIENDとENEMYのみで書いてしまう
        # 返り値はなし
        """
        number_of_friend_unit = 0
        number_of_enemy_unit = 0
        for row in self:
            for square in row:
                if square.unit_exist == True:
                    if square.unit.team == "FRIEND":
                        number_of_friend_unit = number_of_friend_unit + 1
                    elif square.unit.team == "ENEMY":
                        number_of_enemy_unit = number_of_enemy_unit + 1
        self.dictionary["FRIEND"] = number_of_friend_unit
        self.dictionary["ENEMY"] = number_of_enemy_unit
        # print("i am {} and".format(self.name),"reset is called")
        # for test
    def reset_area_occupaied_team(self):
        """
        # self.dictionaryからどちらのユニットが多いのか判定し、
        # self.occupaied_teamを更新する
        # f>e -> f
        # f<e -> e
        # f=e -> None
        """
        number_of_friend_unit = self.dictionary.get("FRIEND")
        number_of_enemy_unit = self.dictionary.get("ENEMY")
        if number_of_friend_unit > number_of_enemy_unit:
            self.occupaied_team = "FRIEND"
        elif number_of_friend_unit < number_of_enemy_unit:
            self.occupaied_team = "ENEMY"
        else:
            self.occupaied_team = None
    def reset_area_information(self):
        """
        area.dictionaryとarea.occupaied_teamを更新する
        """
        self.reset_area_dictionary()
        self.reset_area_occupaied_team()


# {name:[name, coordinate], ... }でデータを持つ
area_dictionary = {
    "CENTRAL_AREA":["CENTRAL_AREA", [2,2]],
    "RIGHT_UPPER_AREA":["RIGHT_UPPER_AREA", [3,1]],
    "LEFT_UPPER_AREA":["LEFT_UPPER_AREA", [1,1]],
    "LEFT_LOWER_AREA":["LEFT_LOWER_AREA", [1,3]],
    "RIGHT_LOWER_AREA":["RIGHT_LOWER_AREA", [3,3]]
}
