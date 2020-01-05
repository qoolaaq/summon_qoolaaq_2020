import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

import game_initilizer



class FieldPanel:
    """
    Fieldの描画のために作る
    Fieldpanel.squareにsquareを代入する
    """
    color_none = (255, 255, 255)
    # いないのはwhite
    color_exist = (0, 0, 0)
    # いるのはblack

    def __init__(self, position: list, size: int):
        self.position = position
        self.size = size
        self.flag = False
        self.color = FieldPanel.color_none
        self.square = None
        # 継承して、FieldFieldPanelに実装させる
        # やっぱりやめた

    def make_flag_change(self):
        """
        flagを反転させて、colorプロパティを変える
        """
        self.flag = not self.flag
        if self.flag == True:
            self.color = FieldPanel.color_exist
        else:
            self.color = FieldPanel.color_none

    def get_square(self, square):
        self.square = square

    def flag_reset(self):
        """
        unit.existがTrueなら、flagをTrueにして描画させる
        """
        self.flag = self.square.unit_exist
        # print("flag.reset is called")
        if self.flag == True:
            self.color = FieldPanel.color_exist
        else:
            self.color = FieldPanel.color_none

class OtherPanel:
    """
    Bench、Outsideの描画のために作る
    panel.unitにunitを代入する
    """
    color_none = (255, 255, 255)
    # いないのはwhite
    # ユニットがいないことを想定してないので、要らないかも
    color_exist = (0, 0, 0)
    # いるのはblack

    def __init__(self, unit, position, number: int, size: int):
        self.position = position
        self.number = number
        self.size = size
        self.flag = False
        self.color = OtherPanel.color_exist
        # ユニットがいるときにしか描写しないから、noneは要らないかも
        self.unit = unit
        # ユニットがいるときにしか描写しないから、予め入れておく

    def get_unit(self, unit):
        """
        unitをself.unitに入れる
        __init__で代入したあと、毎回作っては消すから要らないかも
        """
        self.unit = unit

class OtherPanels(list):
    """
    Bench、Outsideを描画するためのクラス
    listを継承する
    描画する際のpanel_sizeを引数として予め持っておく
    """
    start_panel_position = (350, 30)
    # とりあえずハードコーディングしている
    # ここは改めて変える必要がある(20/01/05)

    def __init__(self, size):
        self.panel_size = size
    def self_reset(self):
        """
        自身のリストの中の要素をすべて削除する
        """
        self.clear()
    def panel_make_from_list(self, list):
        """
        listを読み込んで、その分だけpanelを作成
        panel.unitにユニットを代入する
        """
        for unit in list:
            position_number = unit.position_number_return()
            new_panel = OtherPanel\
                (unit,OtherPanels.start_panel_position, position_number, self.panel_size)
            # 書き直す必要がありそう
            # 描画開始する場所を参照するために、クラス変数を使用している。
            # OtherPanels.start_panel_positionがそれ
            # 絶対書き直す(20/01/05)
            new_panel.get_unit(unit)
            self.append(new_panel)

