import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

import game_initilizer



class FieldPanel:
    """
    # Fieldの描画のために作る
    # Fieldpanel.squareにsquareを代入する
        # self.position = position
        # self.size = size
        # self.flag = False
        # self.color = FieldPanel.color_None
        # self.square = None
    """
    color_FRIEND = (255, 255, 255)
    # いないのはwhite
    color_ENEMY = (0, 0, 0)
    # いるのはblack
    color_None = (160, 160, 160)
    # 初期値は背景色にしておく

    def __init__(self, position: list, size: int):
        self.position = position
        self.size = size
        self.flag = False
        self.color = FieldPanel.color_None
        self.square = None
        # 継承して、FieldFieldPanelに実装させる
        # やっぱりやめた

    def get_square(self, square):
        self.square = square

    def reset_flag(self):
        """
        unit.existがTrueなら、flagをTrueにして描画させる
        """
        self.flag = self.square.unit_exist
        # print("flag.reset is called")
        if self.flag == True:
            # ユニットのチームに応じて、色を変える
            if self.square.unit.team == "FRIEND":
                self.color = FieldPanel.color_FRIEND
            elif self.square.unit.team == "ENEMY":
                self.color = FieldPanel.color_ENEMY
        else:
            # いなければ、背景色と同じにする
            self.color = FieldPanel.color_None

class OtherPanel:
    """
    # Bench、Outsideの描画のために作る
    # panel.unitにunitを代入する
    # 最初から描画しておく
    # 情報の更新等はOtherPanelsで書くかも
        self.position = position
        self.number = number
        self.size = size
        self.flag = False
        self.color = OtherPanel.color_FRIEND
        self.unit = None
    """
    color_FRIEND = (255, 255, 255)
    # いないのはwhite
    color_ENEMY = (0, 0, 0)
    # いるのはblack
    color_None = (160, 160, 160)
    # 初期値は背景色にしておく

    def __init__(self, position, number: int, size: int):
        self.position = position
        self.number = number
        self.size = size
        self.flag = False
        self.color = OtherPanel.color_None
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
            # ユニットがいなければ、背景色にする
            self.flag = False
            self.color = OtherPanel.color_None
        else:
            self.flag = True
            # ユニットがいるならば、チームに応じて、色を変える
            if self.unit.team == "FRIEND":
                self.color = OtherPanel.color_FRIEND
            elif self.unit.team == "ENEMY":
                self.color = OtherPanel.color_ENEMY

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
            GAP_BETWEEN_FIELD_PANES = 10
            # 隣との間を10だけあける
            panel_position = [
                start_panel_position[0] + (size + GAP_BETWEEN_FIELD_PANES) * number,
                start_panel_position[1]
                ]
            # 横に7つ並べている
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

class AreaFrame:
    """
    # エリアの周りを囲む枠
    # どちらの占領下にあるのかを描画するために作る
    # 引数はエリアインスタンス
    """
    color_FRIEND = (255, 255, 255)
    # いないのはwhite
    color_ENEMY = (0, 0, 0)
    # いるのはblack
    color_None = (80, 80, 80)
    # 初期値は背景色にしておく
    area_frame_adjustment_dictionary = {
        "CENTRAL_AREA":     [0, 0],         # central
        "RIGHT_UPPER_AREA": [0, -3],    # RU
        "LEFT_UPPER_AREA":  [-3, 0],     # LU
        "LEFT_LOWER_AREA":  [0, 3],      # LL
        "RIGHT_LOWER_AREA": [3, 0]      # RL
    }
    # 各エリアを描画時に少しずつずらして被りらなくするためのディクショナリ
    FIELD_PANEL_SIZE = 45
    GAP_BETWEEN_FIELD_PANES = 20
    """
    Globalで上手く読み込めなかったのでこっちで宣言している
    うまい方法が見つかれば切り替える(2020/01/12)
    """

    def __init__(self, area):
        """
        self.area: 引数として入れたareaインスタンス
        self.color: 描画する色。初期値は背景と一緒
        self.xxx_yyy_vertex: 描画するために計算した頂点の位置
        self.vertex_list: 上記をまとめたもの[RU, LU, LL, RL]
        """
        self.area = area
        self.color = AreaFrame.color_None
        # 初期値はcolor_Noneにしておく
        self.area.central_coordinate
        self.area_frame_adjustment_list = \
            AreaFrame.area_frame_adjustment_dictionary.get(self.area.name)
        # 各エリアを描画時に少しずつずらして被りらなくするためのリスト
        # この値だけ各vertexをずらしていく
        self.right_upper_vertex = [
            30 + (self.area.central_coordinate[0] + 2) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[0],
            30 + (self.area.central_coordinate[1] - 1) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[1],
        ]
        # 起点(30,30) 
        #   + (中心座標(xpos, ypos) + 中心からの差(+2, -1)) 
        #       * (field_panelの大きさ + panelの間隔)
        #           - panelの間隔 / 2
        #               + かぶらないように調整
        # 他も同様に計算
        # RU(+2, -1)
        # LU(-1, -1)
        # LL(-1, +2)
        # RL(+2, +2)
        self.left_upper_vertex = [
            30 + (self.area.central_coordinate[0] - 1) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[0],
            30 + (self.area.central_coordinate[1] - 1) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[1],
        ]
        self.left_lower_vertex = [
            30 + (self.area.central_coordinate[0] - 1) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[0],
            30 + (self.area.central_coordinate[1] + 2) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[1],
        ]
        self.right_lower_vertex = [
            30 + (self.area.central_coordinate[0] + 2) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[0],
            30 + (self.area.central_coordinate[1] + 2) \
                * (AreaFrame.FIELD_PANEL_SIZE + AreaFrame.GAP_BETWEEN_FIELD_PANES) \
                    - AreaFrame.GAP_BETWEEN_FIELD_PANES / 2 \
                        + self.area_frame_adjustment_list[1],
        ]
        self.vertex_list = [
            self.right_upper_vertex,
            self.left_upper_vertex,
            self.left_lower_vertex,
            self.right_lower_vertex
        ]
        self.change_color_from_occupaied_team()
    def change_color_from_occupaied_team(self):
        """
        self.area.occupaied_teamの情報を取得して、色を変える
        """
        if self.area.occupaied_team == None:
            self.color = AreaFrame.color_None
        elif self.area.occupaied_team == "FRIEND":
            self.color = AreaFrame.color_FRIEND
        elif self.area.occupaied_team == "ENEMY":
            self.color = AreaFrame.color_ENEMY
        # print("my color is ", self.area.occupaied_team)