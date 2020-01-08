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
    最初から描画しておく
    情報の更新等はOtherPanelsで書くかも
    """
    color_none = (255, 255, 255)
    # いないのはwhite
    color_exist = (0, 0, 0)
    # いるのはblack

    def __init__(self, position, number: int, size: int):
        self.position = position
        self.number = number
        self.size = size
        self.flag = False
        self.color = OtherPanel.color_none
        self.unit = None
        # 最初は何もいないので、色はnone、unitもNoneにしておく
    def get_unit(self, unit):
        """
        unitをself.unitに入れる
        __init__で代入したあと、毎回作っては消すから要らないかも
        """
        self.unit = unit
        self.reset_flag_and_color_from_unit()
    def reset_unit(self):
        """
        self.unitをnoneにする
        """
        self.unit = None
        self.reset_flag_and_color_from_unit()
    def reset_flag_and_color_from_unit(self):
        if self.unit == None:
            self.flag = False
            self.color = OtherPanel.color_none
        else:
            self.flag = True
            self.color = OtherPanel.color_exist

class OtherPanels(list):
    """
    Bench、Outsideを描画するためのクラス
    listを継承する
    描画する際のpanel_sizeを引数として予め持っておく
    """
    # start_panel_position = (350, 30)
    # とりあえずハードコーディングしている
    # ここは改めて変える必要がある(20/01/05)

    def __init__(self, draw_list, start_panel_position, size: int):
        """
        描画する対象をdraw_listで受け取り、self.listに入れる
        実際に描画するパネルのサイズをsizeで受け取り、self.sizeに入れる
        self.initializeのために、start_panel_positionも受け取る
        """
        self.list = draw_list
        self.panel_size = size
        self.start_panel_position = start_panel_position
        self.initilize(start_panel_position, size)
    def initilize(self, start_panel_position, size):
        """
        start_panel_position = taple(x, y)
        ゲーム開始時に使うメソッド
        __init__()の方にも書いておく
        """
        for number in range(7):
            # とりあえず現状の手札=7だけ描画する
            panel_position = [start_panel_position[0] + (size + 10) * number, start_panel_position[1]]
            # 隣との間を10だけあける
            panel = OtherPanel(panel_position, number, size)
            self.append(panel)
    def reload_panel_unit(self):
        """
        各panelにユニット情報を更新させる
        unitはself.listから拾ってくる
        """
        self.reset_panel_unit()
        for number in range(len(self.list)):
            # 描画対象のユニットがいる分だけfor文を回す
            unit = self.list[number]
            panel = self[number]
            panel.get_unit(unit)
    def reset_panel_unit(self):
        """
        各panelのユニット情報を消す
        """
        for panel in self:
            panel.reset_unit()
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

