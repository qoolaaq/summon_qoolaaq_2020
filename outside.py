# coding: utf-8

"""
---Outsideについて---
ユニットをリストとして管理する

"""

class Outside(list):
    # teamは文字列としてデータを持っておく
    def __init__(self, team):
        self.team = team
        self.type = "outside"
    
    def type_get(self):
        return self.type

    def receive_unit(self, unit):
        """
        unitをアウトサイドに追加する
        暫定だけれど、unitのポジションタイプ等もいじっておく
        2020/01/19
        """
        # unitを自身のリストの中に入れる
        self.append(unit)
        # unitのプロパティを変更する
        unit.position_type = "outside"
        unit.position_number = self.index(unit)
        unit.position_list_change(
            [unit.position_type, unit.position_number]
        )