# coding: utf-8

from unit import *
from square_field_area import *
from action import *
from bench import *
from outside import *
from action import *

"""
ゲームを始めるときに読み込むモジュール

グローバル変数を参照出来ないので、
引数として全部受け取っておく
"""

"""
スターティングメンバーのリストを作っておく
今はとりあえず書いてる
"""
def friend_starting_menber_list_get():
    return ["Alice", "Becky", "Cashy"]

def game_initialize(ALL_UNIT_LIST, FIELD, \
    ALL_AREA_LIST, ALL_BENCH_LIST, ALL_OUTSIDE_LIST, \
        STARTING_MEMBER_LIST):
    # とりあえずゲームロジックで使う全部の要素を受け取る

    def unit_generate(unit_name, team):
        """
        そのチームのユニットを作る
        """
        return Unit(unit_name, team)
        pass

    def unit_register_to_bench(unit, bench):
        """
        ユニットをベンチに入れる
        引数はユニットとベンチにする
        """
        bench.unit_register(unit)

    def unit_position_list_change_to_bench(unit, bench):
        """
        ユニットのposition_listを変える
        ["bench", number]
        """
        position_list = bench.position_list_get(unit)
        unit.position_list_change(position_list)
        
    def unit_register_to_ALL_UNIT_LIST(unit, ALL_UNIT_LIST):
        """
        ALL_UNIT_LISTにユニットオブジェクトを入れる
        引数はユニットとALL_UNIT_LISTにする
        """
        ALL_UNIT_LIST.append(unit)

    for unit_name in STARTING_MEMBER_LIST:
        unit = unit_generate(unit_name, "FRIEND")
        # 新規にユニットを作る
        unit_register_to_bench(unit, ALL_BENCH_LIST[0])
        # ユニットをベンチに格納していく
        unit_position_list_change_to_bench(unit, ALL_BENCH_LIST[0])
        # ユニットのタイプをベンチにする
        unit_register_to_ALL_UNIT_LIST(unit, ALL_UNIT_LIST)
        # ここはとりあえずざっと書いただけ
        # 後で変える

        # for unit in ALL_BENCH_LIST[0]:
        #     print(unit.name)
        #     print(unit.position_list)