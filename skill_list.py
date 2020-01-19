from skill import *
from skill_parts import *

class SkillOfAlice(Skill):
    def __init__(self):
        super().__init__()
        self.timing_CIF = True
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        """
        自分を対象に取れなくする
        """
        self.unit.chenge_targetable()

class SkillOfBecky(Skill):
    """
    登場時、上下左右のユニットをすべてベンチに送る
    """
    def __init__(self):
        super().__init__()
        self.timing_CIF = True
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        """
        置かれた場所の上下左右のユニットをアウトサイド送りにする
        敵味方関係なし
        """
        unit = self.unit
        target_coordinate_list = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        target_squares_list = select_units_from_list(
            unit, target_coordinate_list, FIELD
            )

        # squareのユニットをアウトサイド送りにする
        # squareにunitがいてtargatableならば処理する
        targetable_target_squares_list = \
            check_unit_exist_from_list(target_squares_list)
    
        send_unit_from_square_to_outside(
            targetable_target_squares_list,
            FIELD,
            ALL_OUTSIDE_LIST,
            SKILL_PROCESSOR
        )

class SkillOfCathy(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfDaisy(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfEmilia(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfFlora(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfGrace(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass



class SkillOfReina(Skill):
    def __init__(self):
        super().__init__()
        self.timing_PIO = True
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        """
        中央squareにunitがいなければ、そこに復活する
        """
        unit = self.unit
        if not FIELD[2][2].unit_exist:
            for outside in ALL_OUTSIDE_LIST:
                if unit in outside:
                    outside.remove(unit)
                    # 2体以上間違えてoutsideに入ってしまうとエラーになりそう
            FIELD[2][2].unit_place(unit)
            unit.position_list_change(["square", 12])

class SkillOfSelena(Skill):
    def __init__(self):
        super().__init__()
        self.timing_CIF = True
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        """
        上下左右のunitを端まで押しやる
        再帰をかけなかったので、とりあえず右のユニットを1マス押しやる
        """
        unit = self.unit
        reference_coordinate = \
            translate_position_number_to_coordinate(unit.position_number)
        target_coordinate_list = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        targetable_target_squares_list = \
            check_unit_exist_from_list(
                select_units_from_list(
                    unit, target_coordinate_list, FIELD
                    )
            )

        for target_square in targetable_target_squares_list:
            # temporary_coordinate = target_square.coordinate
            if target_square.xpos > reference_coordinate[0] and\
                target_square.xpos + 1 <= 4:
                temporary_square = \
                    FIELD[reference_coordinate[1]][target_square.xpos + 1]
                if not temporary_square.is_unit_exist():
                    move_unit_from_square_to_square(
                        target_square.unit, temporary_square, FIELD
                        )


class SkillOfTina(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfVivian(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfWillow(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfYvonne(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass

class SkillOfZara(Skill):
    def __init__(self):
        super().__init__()
    def effect(
        self,
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        SKILL_PROCESSOR
        ):
        pass