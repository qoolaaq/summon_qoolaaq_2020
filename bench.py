# coding: utf-8

"""
---benchについて---
ユニットをリストとして管理する

"""

class Bench(list):
    # teamは文字列としてデータを持っておく
    def __init__(self, team):
        self.team = team
        self.type = "bench"

    def unit_register(self, unit):
        self.append(unit)

    def unit_call(self, bench_number):
        """
        返り値はbench_numberに存在するユニット
        呼び出したユニットはselfから消す
        """
        # unit = self[bench_number]
        # self = self.pop(bench_number)
        unit = self.pop(bench_number)
        return unit

    def position_type_get(self):
        """
        引数はなし
        position_type="bench"を返す
        """
        return self.type

    def position_number_get(self,unit):
        """
        引数はunit、返り値はnumber
        そのユニットがベンチの何番目にいるのか返す
        """
        return self.index(unit)
    
    def position_list_get(self, unit):
        """
        引数はunit、返り値はposition_list
        """
        position_type = self.position_type_get()
        position_number = self.position_number_get(unit)
        return [position_type, position_number]




"""
B = Bench("Friend")
B.unit_register("a")
B.unit_register("b")

print(B)

B.unit_call(0)

print(B)
"""