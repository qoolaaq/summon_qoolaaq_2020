# coding: utf-8

"""
---benchについて---
ユニットをリストとして管理する

"""

class Bench(list):
    # teamは文字列としてデータを持っておく
    def __init__(self, team):
        self.team = team