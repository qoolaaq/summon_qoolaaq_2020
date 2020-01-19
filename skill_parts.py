import math

def translate_position_number_to_coordinate(number):
    """
    numberをcoordinate[xpos, ypos]に変換して返す
    """
    coordinate_x = number % 5
    coordinate_y = math.floor(number / 5)
    coordinate = [
        coordinate_x, coordinate_y
        ]
    return coordinate

def select_units_from_list(reference_unit, target_coordinate_list, FIELD):
    """
    座標のリストを元にして、対象のsquareをフィールドから選ぶ
    返り値はtarget_squares_list
        reference_unit: skillを発動させたユニット
        target_coordinate_list: 対象となるsquareを選ぶためのリスト
            基準点を[0,0]として、[2,3]のように書く
            ex [[1, 0],[0, 1],[-1, 0],[0, -1]]
        FIELD: 多分これがないと怒られる
    """

    target_squares_list = []

    # unit.position_numberからcoordinateに変換
    reference_coordinate = \
        translate_position_number_to_coordinate(reference_unit.position_number)
    reference_coordinate_x = reference_coordinate[0]
    reference_coordinate_y = reference_coordinate[1]

    # [0][0]から[4][4]の範囲になるように、target_squares_listを生成
    for coordinate in target_coordinate_list:
        if (0 <= reference_coordinate_x + coordinate[0] <= 4) and\
            (0 <= reference_coordinate_y + coordinate[1] <= 4):
            target_squares_list.append(
                FIELD[reference_coordinate_y + coordinate[1]][reference_coordinate_x + coordinate[0]]
            )

    return target_squares_list

def check_unit_exist_from_list(target_squares_list):
    """
    target_squares_list内で、選択可能なユニットがいるsquareのみ選んで、
    targetable_target_squares_listとして返す
    """
    targetable_target_squares_list = []
    for square in target_squares_list:
        if square.is_unit_exist() and square.unit.is_targetable():
            targetable_target_squares_list.append(square)
    return targetable_target_squares_list

def send_unit_from_square_to_outside(
    targetable_target_squares_list,
    FIELD,
    ALL_OUTSIDE_LIST,
    SKILL_PROCESSOR
    ):
    """
    targetable_target_squares_listのユニットをベンチに送る
    """
    for square in targetable_target_squares_list:
        target_unit = square.unit
        square.delete_unit()
        if target_unit.team == "FRIEND":
            ALL_OUTSIDE_LIST[0].receive_unit(target_unit)    
        elif target_unit.team == "ENEMY":
            ALL_OUTSIDE_LIST[1].receive_unit(target_unit)
        if target_unit.skill.is_activated("PIO"):
            SKILL_PROCESSOR.load_skill(target_unit.skill)

def move_unit_from_square_to_square(unit, target_square, FIELD):
    """
    unitをtarget_squareに置く
    """
    current_coordinate = \
        translate_position_number_to_coordinate(
            unit.position_number
            )
    current_square = \
        FIELD[current_coordinate[1]][current_coordinate[0]]
    current_square.delete_unit()
    target_square.unit_place(unit)
    unit.position_list_change(target_square.position_list)

    print("##########################################i am read")
