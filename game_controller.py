# coding: utf-8

from unit import *
from square_field_area import *
from action import *
from bench import *
from outside import *
from action import *

class GameController:
    """
    # mainから座標を受け取って、残り全ての動作をここで行う
    # グローバル変数を参照出来ないので、
    # 引数として全部受け取っておく
    """
    def progress_game(
        ALL_UNIT_LIST,
        FIELD,
        ALL_AREA_LIST,
        ALL_BENCH_LIST,
        ALL_OUTSIDE_LIST,
        STARTING_MEMBER_LIST,
        click_position
        ):
        """
        # click_positionはクリックした座標
        # [2, 3]みたいな形で取得する
        """

        clicked_square = \
            FIELD[click_position[1]][click_position[0]]
        # 指定した座標のsquareを、clicked_squareとして持っておく

        def clicked_unit_call_from_bench(bench):
            """
            # クリック時にbench[0]からユニットを持ってくる
            # 返り値はユニットオブジェクト
            # 他のベンチのユニットのposition_listをここで更新する
            """
            unit = bench.unit_call(0)
            unit.position_list_change([None, None])
            # 常に先頭を持ってくるので、0を引数とする

            # print("i am called and my name is ", unit.name)
            # # for test
            # # だれが置かれるのか書き出す
            for left_unit in bench:
                # print("i am ", left_unit.name, " in bench")
                # # for test
                # # benchに誰がいるのか書き出す
                position_list = bench.position_list_get(left_unit)
                left_unit.position_list_change(position_list)
            return unit

        def clicked_unit_place_to_square(unit):
            """
            ユニットオブジェクトをclicked_squareに置く
            """
            clicked_square.unit_place(unit)

        def unit_position_list_change(unit):
            """
            clicked_unitのposition_listをclick_positionに変える
            """
            list = clicked_square.position_list_get()
            unit.position_list_change(list)

        def clickable_check():
            """
            クリックされた座標のsquareにおけるのか確認
            unit_existがTrueならFalseを返す
            """
            return not clicked_square.unit_placable_get()
        
        def reset_all_area_information():
            """
            すべてのエリアのarea.dictionaryを更新する
            """
            for area in ALL_AREA_LIST:
                area.reset_area_information()
                print(
                    "i am {}".format(area.name),
                    " and my dict is",
                    area.dictionary,
                    "and i am occupaied by",
                    area.occupaied_team
                    )
                # for test

        """
        メインの動作
        """
        if clickable_check():
            # ユニットがいないsquareのみに置ける

            if not len(ALL_BENCH_LIST[1]) == 0:
            # ベンチにユニットがいるときのみ置くようにした

                #####
                # FRIEND_BENCH >= ENEMY_BENCHならば、FRIEND＿BENCHからユニットを出す
                # そうでなければ、ENEMY_BENCHからユニットを出す
                #####
                if len(ALL_BENCH_LIST[0]) >= len(ALL_BENCH_LIST[1]):
                    unit = clicked_unit_call_from_bench(ALL_BENCH_LIST[0])
                else:
                    unit = clicked_unit_call_from_bench(ALL_BENCH_LIST[1])
                # ベンチの先頭のユニットをunitに代入

                clicked_unit_place_to_square(unit)
                # squareにユニットを置く

                unit_position_list_change(unit)
                # unitのposition_listを更新

                """
                # for test
                """
                for unit in ALL_UNIT_LIST:
                    print("#####")
                    print("my name is", unit.name)
                    print("my team is", unit.team)
                    print("i am in", unit.position_list)
                    print("#####")


                reset_all_area_information()
                # areaの情報を更新(area.reset_area_dictionary)
