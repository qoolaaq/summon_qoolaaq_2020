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
CENTRAL_AREA = Area(FIELD, "central_area")
RIGHT_UPPER_AREA = Area(FIELD, "right_upper_area")
LEFT_UPPER_AREA = Area(FIELD, "left_upper_area")
LEFT_LOWER_AREA = Area(FIELD, "left_lower_area")
RIGHT_LOWER_AREA = Area(FIELD, "right_lower_area")
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
FRIEND_BENCH = Bench("FRIEND")
ENEMY_BENCH = Bench("ENEMY")
ALL_BENCH_LIST = [
    FRIEND_BENCH,
    ENEMY_BENCH
    ]
# アウトサイド
FRIEND_OUTSIDE = Outside("FRIEND")
ENEMY_OUTSIDE = Outside("ENEMY")
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
FIELD_PANEL_SIZE = 50
FIELD_PANELS = \
    [[FieldPanel(
        [30 + i * (FIELD_PANEL_SIZE + 10), 30 + j * (FIELD_PANEL_SIZE + 10)],FIELD_PANEL_SIZE)\
         for i in range(5)] for j in range(5)]
# フィールドを表示するパネルを生成する
# [30, 30]はパネルの開始地点
# パネル間を10としている

BENCH_PANEL_SIZE = 30
OUTSIDE_PANEL_SIZE = 30
FRIEND_BENCH_PANELS = OtherPanels(
    FRIEND_BENCH,
    [350, 30],
    BENCH_PANEL_SIZE
    )
FRIEND_OUTSIDE_PANELS = OtherPanels(
    FRIEND_OUTSIDE,
    [350, 70],
    BENCH_PANEL_SIZE
    )

ENEMY_BENCH_PANELS = OtherPanels(
    ENEMY_BENCH,
    [350, 150],
    BENCH_PANEL_SIZE
    )
ENEMY_OUTSIDE_PANELS = OtherPanels(
    ENEMY_OUTSIDE,
    [350, 190],
    BENCH_PANEL_SIZE
    )

ALL_OTHER_PANELS = [
    FRIEND_BENCH_PANELS,
    FRIEND_OUTSIDE_PANELS,
    ENEMY_BENCH_PANELS,
    ENEMY_OUTSIDE_PANELS
    ]



# """
# PANELとGameLogicを紐付けていく
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
for other_panels in ALL_OTHER_PANELS:
    other_panels.reload_panel_unit()


"""
以下、メインルーティン
"""
def main():

    sysfont = pygame.font.SysFont(None, 50)
    mousepos = []
    # ここにマウスがクリックされたときの座標情報がタプルとして入る

    while True:
        SURFACE.fill((80, 80, 80))
        # SURFACEの中身をタプル()で塗りつぶす
        # (R,G,B)
        # (255,255,255)で白

        """
        PAFIELD_PANELSの描画
        """
        # 試験的に、panelの背景を作っている
        for row in FIELD_PANELS:
            for panel in row:
                # 試験的に、panelの背景を作っている
                pygame.draw.rect(
                    SURFACE, 
                    (160, 160, 160), 
                    (panel.position[0]-2.5, 
                    panel.position[1]-2.5, 
                    panel.size + 5, 
                    panel.size + 5)
                    )

                # こちらが実際のpanel
                pygame.draw.rect(
                    SURFACE, 
                    panel.color, 
                    (panel.position[0], 
                    panel.position[1], 
                    panel.size, 
                    panel.size)
                    )
                # panel.position -> [xpos, ypos]

        """
        OTHER_PANELSの描画
        """
        for panels in ALL_OTHER_PANELS:
            for panel in panels:
                # 試験的に、panelの背景を作っている
                pygame.draw.rect(
                    SURFACE, 
                    (160, 160, 160), 
                    (panel.position[0]-2, 
                    panel.position[1]-2, 
                    panel.size + 4, 
                    panel.size + 4)
                    )

                pygame.draw.rect(
                    SURFACE, 
                    panel.color, 
                    (panel.position[0], 
                    panel.position[1], 
                    panel.size, 
                    panel.size)
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
                for row in FIELD_PANELS:
                    for panel in row:
                        # print("test {}".format(event.pos))
                        if (panel.position[0] < event.pos[0] < panel.position[0] + panel.size)  \
                            and (panel.position[1] < event.pos[1] < panel.position[1] + panel.size):
                            # マウスが動かされた場所がpaneleの範囲内なら、その座標をmouse_positionに入れる
                            mouse_position = panel.square.coordinate
                            if panel.square.unit_exist:
                                print(panel.square.unit.name)
                # とりあえずFRIEND_BENCH_PANELだけマウスオーバーを実装
                # 似たような記述なので、統合したい(2020/01/08)
                for panels in ALL_OTHER_PANELS:
                    for panel in panels:
                        if (panel.position[0] < event.pos[0] < panel.position[0] + panel.size)  \
                                and (panel.position[1] < event.pos[1] < panel.position[1] + panel.size):
                                if panel.flag == True:
                                    print(panel.unit.name)
            elif event.type == MOUSEBUTTONDOWN:
                # mousepos.append(event.pos)
                # マウスの座標＝event.posでタプルとして取得
                for row in FIELD_PANELS:
                    for panel in row:
                        # print("test {}".format(event.pos))
                        if (panel.position[0] < event.pos[0] < panel.position[0] + panel.size)  \
                            and (panel.position[1] < event.pos[1] < panel.position[1] + panel.size):
                            # クリックされた場所がpaneleの範囲内なら、その座標をclick_positionに入れる
                            click_position = panel.square.coordinate

                            print("clicked position is", click_position)
                            # for test
                            # ちゃんと指定したところに描写されているのか
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
                            # とりあえず今はFRIENDのユニットのみを出している

                            """
                            描画を更新する
                            """
                            for other_panels in ALL_OTHER_PANELS:
                                other_panels.reload_panel_unit()

                            # FRIEND_BENCH_PANELS.panel_make_from_list(FRIEND_BENCH)
                            # # ターンが終わり次第、各OTHER_PANELSの中身をリセットする
                            # # とりあえずFRIEND_BENCH_PANELSのみ処理する
                            # # とりあえずFRIEND_BENCH_PANELSのみ描画する
                            # # あとで他のOTHER_PANELSも処理する(20/01/05)
        """
        描画を更新する
        """
        for row in FIELD_PANELS:
            for field_panel in row:
                field_panel.reset_flag()
        # FIELD_PANELの描写の更新
        
        # for panel in FRIEND_BENCH_PANELS:
        #     pygame.draw.rect(SURFACE, panel.color, \
        #         (panel.position[0] + panel.number * 40, panel.position[1], panel.size, panel.size))
        # # とりあえずFRIEND_BENCH_PANELSのみ描画する
        # # あとで他のOTHER_PANELSも描画する(20/01/05)

        pygame.display.update()
        # プログラム内で描画した内容を反映させる
        FPSCLOCK.tick(10)
        # 1秒間に10回ループを回す

if __name__ == "__main__":
    main()
