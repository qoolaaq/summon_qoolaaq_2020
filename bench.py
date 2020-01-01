# coding: utf-8

"""
---benchについて---
ユニットをリストとして管理する

"""

class Bench():
    # teamは文字列としてデータを持っておく
    def __init__(self, team):
        self.list = []
        self.team = team
