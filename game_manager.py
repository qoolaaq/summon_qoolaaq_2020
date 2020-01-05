# coding: utf-8

from unit import *
from square_field_area import *
from action import *
from bench import *
from outside import *
from action import *

"""
mainから座標を受け取って、残り全ての動作をここで行う
グローバル変数を参照出来ないので、
引数として全部受け取っておく
"""

def game_manage(ALL_UNIT_LIST, FIELD, \
    ALL_AREA_LIST, ALL_BENCH_LIST, ALL_OUTSIDE_LIST, \
        STARTING_MEMBER_LIST, click_position):
    # click_positionはクリックした座標
    # [2, 3]みたいな形で取得する

    clicked_square = \
        FIELD[click_position[1]][click_position[0]]
    # 指定した座標のsquareを、clicked_squareとして持っておく

    def clicked_unit_call_from_bench(bench):
        """
        クリック時にbench[0]からユニットを持ってくる
        返り値はユニットオブジェクト
        他のベンチのユニットのposition_listをここで更新する
        """
        unit = bench.unit_call(0)
        unit.position_list_change([None, None])
        # 常に先頭を持ってくるので、0を引数とする
        print("i am called and my name is ", unit.name)
        # for test
        for left_unit in bench:
            print("i am ", left_unit.name, " in bench")
            # for test
            position_list = bench.position_list_get(left_unit)
            left_unit.position_list_change(position_list)
        return unit

    def clicked_unit_place_to_square(unit):
        """
        ユニットオブジェクトをclicked_squareに置く
        """
        clicked_square.unit_place(unit)

    def unit_position_list_change(unit):
        list = clicked_square.position_list_get()
        unit.position_list_change(list)

    def clickable_check():
        # クリックされた座標のsquareにおけるのか確認
        # 返り値はbool
        return not clicked_square.unit_placable_get()

    if clickable_check():
        # ユニットがいないsquareのみに置ける
        
        # for test
        print("bench menber is")
        for unit in ALL_BENCH_LIST[0]:
            print(unit.name)

        unit = clicked_unit_call_from_bench(ALL_BENCH_LIST[0])
        print("clicked to called unit is", unit.name)
        print("clicked_square.position_list is ", clicked_square.position_list)
        print("pre unit.position_list is", unit.position_list)
        clicked_unit_place_to_square(unit)
        unit_position_list_change(unit)
        print("clicked_square.position_list is ", clicked_square.position_list)
        print("post unit.position_list is", unit.position_list)
        # for test
        # ベンチ内のユニットの所在を見る
        # for unit in ALL_BENCH_LIST[0]:
        #     print(unit.name)
        #     print(unit.position_list)
        for unit in ALL_UNIT_LIST:
            print(unit.name)
            print(unit.position_list)