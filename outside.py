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
