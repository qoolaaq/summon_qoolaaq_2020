# coding: utf-8

from unit import *
from square_field_area import *
from player import *
from bench import *
from outside import *
from player import *

"""
---問題---
unit_exist_resetが機能しない
fieldとALL_UNIT_LISTが定義されないのがきつい
構造上の問題な気がする
変数のスコープがややこしくなっているので、ほどく必要がある
"""

# グローバル変数を宣言していく
# すべてのユニットをALL_UNIT_LISTに入れる
ALL_UNIT_LIST = []
# フィールド
FIELD = Field()
# 各エリアを作成する
CENTRAL_AREA = Area(FIELD, AreaInformationListGetter("central_area"))
RIGHT_UPPER_AREA = Area(FIELD, AreaInformationListGetter("right_upper_area"))
LEFT_UPPER_AREA = Area(FIELD, AreaInformationListGetter("left_upper_area"))
LEFT_LOWER_AREA = Area(FIELD, AreaInformationListGetter("left_lower_area"))
RIGHT_LOWER_AREA = Area(FIELD, AreaInformationListGetter("right_lower_area"))
# ベンチ
BENCH = Bench("friend")
# アウトサイド
OUTSIDE = Outside("friend")

# unit_maker("Alice", "friend", ["field", 0])
Alice = Unit("Alice", "friend", ["field", 0])

# Alice = unit_maker("Alice", "friend", ["field", 0])
ALL_UNIT_LIST.append(Alice)
FIELD.list[0][0].unit_placed(Alice)

print(id(LEFT_UPPER_AREA.list[0][0].unit))
print(id(FIELD.list[0][0].unit))
print(id(Alice))