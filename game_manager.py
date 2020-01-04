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


##### ここを書く ######
def game_manage(ALL_UNIT_LIST, FIELD, \
    ALL_AREA_LIST, ALL_BENCH_LIST, ALL_OUTSIDE_LIST, \
        STARTING_MEMBER_LIST, click_position):
    # click_positionはクリックした座標
    # [2, 3]みたいな形で取得する

    def unit_place(unit, click_position):
        """
        click_positionの座標にunitを置く
        """
        pass
    pass