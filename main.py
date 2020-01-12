# coding: utf-8

import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN, MOUSEMOTION

from unit import *
from square_field_area import *
from action import *
from bench import *
from outside import *
from action import *
from input import *
from drawer import *
from game_controller import *
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
CENTRAL_AREA        = Area(FIELD, "CENTRAL_AREA")
RIGHT_UPPER_AREA    = Area(FIELD, "RIGHT_UPPER_AREA")
LEFT_UPPER_AREA     = Area(FIELD, "LEFT_UPPER_AREA")
LEFT_LOWER_AREA     = Area(FIELD, "LEFT_LOWER_AREA")
RIGHT_LOWER_AREA    = Area(FIELD, "RIGHT_LOWER_AREA")
# 全てのエリアを統括するリストを作成する
# 中央から反時計周りで格納する
ALL_AREA_LIST = [
    CENTRAL_AREA,
    RIGHT_UPPER_AREA,
    LEFT_UPPER_AREA,
    LEFT_LOWER_AREA,
    RIGHT_LOWER_AREA
]

# ベンチ
FRIEND_BENCH    = Bench("FRIEND")
ENEMY_BENCH     = Bench("ENEMY")
ALL_BENCH_LIST = [
    FRIEND_BENCH,
    ENEMY_BENCH
    ]
# アウトサイド
FRIEND_OUTSIDE  = Outside("FRIEND")
ENEMY_OUTSIDE   = Outside("ENEMY")
ALL_OUTSIDE_LIST = [
    FRIEND_OUTSIDE,
    ENEMY_OUTSIDE
    ]

"""
ゲームロジックを初期化する
"""

# STARTING_MEMBER_LISTを作成
FRIEND_STARTING_MEMBER_LIST = \
    GameInitializer.friend_starting_menber_list_get()
ENEMY_STARTING_MEMBER_LIST = \
    GameInitializer.enemy_starting_menber_list_get()
STARTING_MEMBER_LIST = [
    FRIEND_STARTING_MEMBER_LIST,
    ENEMY_STARTING_MEMBER_LIST
]

# GameInitializerに初期化をさせる
GameInitializer.initialize_game(
    ALL_UNIT_LIST,
    FIELD,
    ALL_AREA_LIST,
    ALL_BENCH_LIST,
    ALL_OUTSIDE_LIST,
    STARTING_MEMBER_LIST
    )


"""
GameLogicの描画で使うオブジェクトをここで宣言しておく
"""
FIELD_PANEL_SIZE = 45
# 各field_panelの大きさ
GAP_BETWEEN_FIELD_PANES = 20
# field_panelの間隔の大きさ

FIELD_PANELS = \
    [[FieldPanel(
        [30 + i * (FIELD_PANEL_SIZE + GAP_BETWEEN_FIELD_PANES),
        30 + j * (FIELD_PANEL_SIZE + GAP_BETWEEN_FIELD_PANES)],
        FIELD_PANEL_SIZE)\
         for i in range(5)] 
         for j in range(5)]
# フィールドを表示するパネルを生成する
# [30, 30]はパネルの開始地点

BENCH_PANEL_SIZE = 30
OUTSIDE_PANEL_SIZE = 30

FRIEND_BENCH_PANELS = OtherPanels(
    FRIEND_BENCH,
    [360, 40], # panelを描画する開始点
    BENCH_PANEL_SIZE
    )
FRIEND_OUTSIDE_PANELS = OtherPanels(
    FRIEND_OUTSIDE,
    [360, 80],
    BENCH_PANEL_SIZE
    )
ENEMY_BENCH_PANELS = OtherPanels(
    ENEMY_BENCH,
    [360, 130],
    BENCH_PANEL_SIZE
    )
ENEMY_OUTSIDE_PANELS = OtherPanels(
    ENEMY_OUTSIDE,
    [360, 170],
    BENCH_PANEL_SIZE
    )

ALL_OTHER_PANELS_LIST = [
    FRIEND_BENCH_PANELS,
    FRIEND_OUTSIDE_PANELS,
    ENEMY_BENCH_PANELS,
    ENEMY_OUTSIDE_PANELS
    ]

CENTRAL_AREA_FRAME      = AreaFrame(CENTRAL_AREA)
RIGHT_UPPER_AREA_FRAME  = AreaFrame(RIGHT_UPPER_AREA)
LEFT_UPPER_AREA_FRAME   = AreaFrame(LEFT_UPPER_AREA)
LEFT_LOWER_AREA_FRAME   = AreaFrame(LEFT_LOWER_AREA)
RIGHT_LOWER_AREA_FRAME  = AreaFrame(RIGHT_LOWER_AREA)

ALL_AREA_FRAME_LIST = [
    CENTRAL_AREA_FRAME,
    RIGHT_UPPER_AREA_FRAME,
    LEFT_UPPER_AREA_FRAME,
    LEFT_LOWER_AREA_FRAME,
    RIGHT_LOWER_AREA_FRAME
]

# """
# PANELSやFRAMESとGameLogicを紐付けていく
# """

"""
FIELD_PANELSとFIELDを紐付ける
具体的には、panel.squareとして情報を持っておく
"""
for i in range(5):
    for j in range(5):
        # FIELD_PANELS[j][i].get_square(FIELD.list[j][i])
        FIELD_PANELS[j][i].get_square(FIELD[j][i])

"""
OTHER_PANELSとBENCHやOUTSIDEを紐付ける
"""
for other_panels in ALL_OTHER_PANELS_LIST:
    other_panels.reload_panel_unit()



def main():
    """
    メインルーティン
    """

    sysfont = pygame.font.SysFont(None, 50)

    while True:
        """
        描画に必要なものはこれですべて管理する
        """
        Drawer.draw_for_routine(
            SURFACE,
            FIELD_PANELS,
            ALL_OTHER_PANELS_LIST,
            ALL_AREA_FRAME_LIST
            )

        for event in pygame.event.get():
            # print(event) ### for test
            # イベントキューからイベントを取得する
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #####
            # ここで、マウスのクリックを座標に変換する
            #####
            elif event.type == MOUSEMOTION:
                mouse_coordinate = event.pos
                """
                # 現在のpanel上でのユニット名をprintする
                """
                Drawer.draw_for_mouse_over_on_panels(
                    SURFACE,
                    FIELD_PANELS,
                    ALL_OTHER_PANELS_LIST,
                    ALL_AREA_FRAME_LIST,
                    mouse_coordinate
                )
            elif event.type == MOUSEBUTTONDOWN:
                # マウスの座標＝event.posでタプルとして取得
                for row in FIELD_PANELS:
                    for panel in row:
                        # print("test {}".format(event.pos))
                        # # for test
                        if (panel.position[0] < event.pos[0] < panel.position[0] + panel.size)  \
                            and (panel.position[1] < event.pos[1] < panel.position[1] + panel.size):

                            click_position = panel.square.coordinate
                            # クリックされた場所がpaneleの範囲内なら、その座標をclick_positionに入れる

                            # print("clicked position is", click_position)
                            # # for test
                            # # ちゃんと指定したところに描写されているのかtest
                            """
                            ここで、panel.square.position_coordinateをLogic側に渡す
                            GameLogicを実際に動かす
                            """
                            GameController.progress_game(
                                ALL_UNIT_LIST,
                                FIELD,
                                ALL_AREA_LIST,
                                ALL_BENCH_LIST,
                                ALL_OUTSIDE_LIST,
                                FRIEND_STARTING_MEMBER_LIST,
                                click_position
                            )

                            """
                            描画を更新する
                            """
                            Drawer.update_instances_for_draw(
                                FIELD_PANELS,
                                ALL_OTHER_PANELS_LIST,
                                ALL_AREA_FRAME_LIST
                            )
                            # ターンが終わり次第、各PANELSとFRAMESをリセットする
        """
        描画を更新する
        """

        pygame.display.update()
        # プログラム内で描画した内容を反映させる
        FPSCLOCK.tick(10)
        # 1秒間に10回ループを回す

if __name__ == "__main__":
    main()