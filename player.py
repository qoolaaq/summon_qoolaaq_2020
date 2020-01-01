# coding: utf-8


class Player():
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

    def get_square_from_number(number):
        # フィールドから目的のスクエアを拾ってくる
        # 返り値はスクエアオブジェクト
        global field 
        """
        ここで怒られる。
        """
        for row in field:
            for square in row:
                if square.number == number:
                    return square

    def unit_maker(data_list, team, position_list):
        # Unitを使ってユニットオブジェクトを作る
        # square.unitにオブジェクトを入れる
        # all_unit_listにオブジェクトを追加する
        global Unit
        """
        ここで怒られる
        """
        self = Unit(data_list, team, position_list)                    
        square = get_square_from_number(position_list[1])
        square.unit_placed(self)
