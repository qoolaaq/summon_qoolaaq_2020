# coding: utf-8

from unit import *
from square_field_area import *
from bench import *
from outside import *
# from main import *

def unit_transfer(unit, post_position_list):
    """
    ---UnitTransfer---
    フィールド、ベンチ、アウトサイドにおいて、ユニットをある場所から他の場所に移す作業を総括的に管理するクラス
    引数として、ユニットオブジェクト、移動後の場所を受け取る
    ユニットオブジェクトを、移動前の場所から移動後の場所へと動かす

    移動したあと、各エリアに情報の更新を要求する?
    """
    # 現在の場所を記録しておく
    # position_list: [position_type, position_number]
    current_position_list = unit.position_list
    # unit.position_listをpre_position_listに変更
    unit.position_list = post_position_list
    unit.position_type = unit.position_list[0]
    unit.position_number = unit.position_list[1]

def get_square_from_number(number, FIELD):
    # フィールドから目的のスクエアを拾ってくる
    # 返り値はスクエアオブジェクト
    """
    ここで怒られる。
    """
    for row in FIELD:
        for square in row:
            if square.number == number:
                return square

def unit_maker(unit_name, team, position_list, ALL_UNIT_LIST):
    # Unitを使ってユニットオブジェクトを作る
    # square.unitにオブジェクトを入れる
    # ALL_UNIT_LISTにオブジェクトを追加する
    global Unit
    global Square
    global Bench
    global Outside

    unit = Unit(unit_name, team, position_list)
    # Unitを使ってユニットオブジェクトを作る

    # return unit

    ALL_UNIT_LIST.append(unit)
    # ALL_UNIT_LISTにunitを追加する

    """
    position_type = position_list[0]
    position_number = position_list[1]
    xpos = position_number % 5
    ypos = (position_number - xpos) / 5
    square = FIELD[ypos][xpos]
    # position_numberからxposとyposに変換
    # squareをFIELDオブジェクトから拾ってくる
    
    square.unit_placed(unit)
    # unit_placedメソッドでスクエアの情報を更新する
    """
