# coding: utf-8


"""
---UnitTransfer---
フィールド、ベンチ、アウトサイドにおいて、ユニットをある場所から他の場所に移す作業を総括的に管理するクラス
引数として、ユニットオブジェクト、移動後の場所を受け取る
ユニットオブジェクトを、移動前の場所から移動後の場所へと動かす

移動したあと、各エリアに情報の更新を要求する?
"""

def UnitTransfer(unit, post_position_list):
    # 現在の場所を記録しておく
    # position_list: [position_type, position_number]
    current_position_list = unit.position_list
    # unit.position_listをpre_position_listに変更
    unit.position_list = post_position_list
    unit.position_type = unit.position_list[0]
    unit.position_number = unit.position_list[1]

def UnitExistChecker():
    # すべてのスクエアのunit_existをリセットする    
    """
    class Field():
        def __init__(self):
            # このあたり事故る可能性ある
            # coordinate = [xpos, ypos], [ypos][xpos]となる
            self.list = [[Square([i,j]) for i in range(5)] for j in range(5)]
    """
    
    """
    for row in field.list:
        for square in row:
            square.unit_exist_checker
    """
    
    """
    # これは動く
    # 引数として、スクエアを引っ張ってくる
    def unit_exist_checker(square):
        square.unit_exist = False
        for unit in all_unit_list:
            if square.position_number == unit.position_number:
                square.unit_exist = True

    for row in field.list:
            for square in row:
                square.unit_exist_checker(square)
    """

def unit_exist_checker(square):
    square.unit_exist = False
    for unit in all_unit_list:
        if square.position_number == unit.position_number:
            square.unit_exist = True
