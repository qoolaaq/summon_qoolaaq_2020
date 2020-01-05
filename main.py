# coding: utf-8

import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

from unit import *
from square_field_area import *
from action import *
from bench import *
from outside import *
from action import *
from input import *
from drawer import *
from game_manager import *
from game_initilizer import *

pygame.init()
# pygameを使うアプリでは必ず最初に呼び出す必要がある

"""
描画で使うオブジェクトをここで宣言しておく
"""
WIDTH = 640
HEIGHT = 360
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
# サイズを指定してウィンドウを表示
# 引数は(WIDTH, HEIGHT)
TITLE = "summon_qoolaaq"
pygame.display.set_caption(TITLE)
# ウィンドウのタイトル
FPSCLOCK = pygame.time.Clock()
# クロックオブジェクトを作り、変数をFPSCLOCKに格納する

"""
GameLogicで使うオブジェクトをここで宣言しておく
"""
# すべてのユニットをALL_UNIT_LISTに入れる
ALL_UNIT_LIST = []
# フィールド
# FIELD = field_maker()
FIELD = Field()
# 各エリアを作成する
CENTRAL_AREA = Area(FIELD, "central_area")
RIGHT_UPPER_AREA = Area(FIELD, "right_upper_area")
LEFT_UPPER_AREA = Area(FIELD, "left_upper_area")
LEFT_LOWER_AREA = Area(FIELD, "left_lower_area")
RIGHT_LOWER_AREA = Area(FIELD, "right_lower_area")
# 全てのエリアを統括するリストを作成する
# 中央から反時計周りで格納する
ALL_AREA_LIST = [CENTRAL_AREA, RIGHT_UPPER_AREA,LEFT_UPPER_AREA, \
    LEFT_LOWER_AREA, RIGHT_UPPER_AREA]
# ベンチ
FRIEND_BENCH = Bench("friend")
ALL_BENCH_LIST = [FRIEND_BENCH]
# アウトサイド
FRIEND_OUTSIDE = Outside("friend")
ALL_OUTSIDE_LIST = [FRIEND_OUTSIDE]

"""
GameLogicの描画で使うオブジェクトをここで宣言しておく
"""
FIELD_PANEL_SIZE = 50
FIELD_PANELS = \
    [[Panel([30 + i * (FIELD_PANEL_SIZE + 10), 30 + j * (FIELD_PANEL_SIZE + 10)],\
         FIELD_PANEL_SIZE)\
         for i in range(5)] for j in range(5)]
# フィールドを表示するパネルを生成する
# [30, 30]はパネルの開始地点
# パネル間を10としている


"""
PANELとGameLogicを紐付けていく
"""

"""
FIELD_PANELSとFIELDを紐付ける
具体的には、panel.squareとして情報を持っておく
"""
for i in range(5):
    for j in range(5):
        # FIELD_PANELS[j][i].get_square(FIELD.list[j][i])
        FIELD_PANELS[j][i].get_square(FIELD[j][i])

"""
ゲームロジックを初期化する
"""
FRIEND_STARTING_MEMBER_LIST = \
    friend_starting_menber_list_get()
game_initialize(ALL_UNIT_LIST, FIELD, \
    ALL_AREA_LIST, ALL_BENCH_LIST, ALL_OUTSIDE_LIST, \
        FRIEND_STARTING_MEMBER_LIST)

# for test
print("game is started")
for unit in ALL_UNIT_LIST:
    print(unit.name)
    print(unit.position_list)

"""
以下、メインルーティン
"""
def main():

    sysfont = pygame.font.SysFont(None, 50)
    mousepos = []
    # ここにマウスがクリックされたときの座標情報がタプルとして入る

    while True:
        SURFACE.fill((128, 128, 128))
        # SURFACEの中身をタプル()で塗りつぶす
        # (R,G,B)
        # (255,255,255)で白

        """
        PAFIELD_PANELSの描画
        """
        for row in FIELD_PANELS:
            for panel in row:
                pygame.draw.rect(SURFACE, panel.color, (panel.position[0], panel.position[1], panel.size, panel.size))
                # panel.position -> [xpos, ypos]

        for event in pygame.event.get():
            # print(event) ### for test
            # イベントキューからイベントを取得する
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #####
            # ここで、マウスのクリックを座標に変換する
            #####
            elif event.type == MOUSEBUTTONDOWN:
                # mousepos.append(event.pos)
                # マウスの座標＝event.posでタプルとして取得
                for row in FIELD_PANELS:
                    for panel in row:
                        # print("test {}".format(event.pos))
                        if (panel.position[0] < event.pos[0] < panel.position[0] + panel.size)  \
                            and (panel.position[1] < event.pos[1] < panel.position[1] + panel.size):
                            # クリックされた場所がpaneleの範囲内なら、そのpanelのmake_flag_changeを行う
                            panel.make_flag_change()
                            print(panel.square.coordinate)
                            # for test
                            # ちゃんと指定したところに描写されているのか
                            """
                            ここで、panel.square.position_coordinateをLogic側に渡す。
                            """
                            click_position = panel.square.coordinate
                            game_manage(ALL_UNIT_LIST, FIELD, ALL_AREA_LIST, ALL_BENCH_LIST, ALL_OUTSIDE_LIST, FRIEND_STARTING_MEMBER_LIST, click_position)
                            # とりあえず今はFRIENDのユニットのみを出している
                            """
                            for test
                            """
                            # print(panel.square.unit.name)
                            # print(panel.square.unit.position_type)
        pygame.display.update()
        # プログラム内で描画した内容を反映させる
        FPSCLOCK.tick(10)
        # 1秒間に10回ループを回す

if __name__ == "__main__":
    main()
