# coding: utf-8

from unit import *
from square_field_area import *
from bench import *
from outside import *
from unit_transfer import *

"""
---問題---
unit_exist_checkerが機能しない
fieldとall_unit_listが定義されないのがきつい
構造上の問題な気がする
変数のスコープがややこしくなっているので、ほどく必要がある
"""

all_unit_list = []

Alice = UnitMaker("Alice", "friend", ["field", 0])

print(field.list[0][0].unit_exist)

"""
# これは動く
# 引数として、スクエアを引っ張ってくる
def unit_exist_checker(square):
    square.unit_exist = False
    for unit in all_unit_list:
        if square.position_number == unit.position_number:
            square.unit_exist = True
"""

unit_exist_checker(field.list[0][0])

print(field.list[0][0].unit_exist)

UnitTransfer(Alice, ["field", 1])
unit_exist_checker(field.list[0][0])


print(field.list[0][0].unit_exist)
