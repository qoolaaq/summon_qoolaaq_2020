import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

import game_initilizer
from panel_frame import *
from unit_information_panel import *

class Drawer:
    """
    描画周りを全部やってもらう
    引数は
        SURFACE,
        FIELD_PANELS,
        ALL_OTHER_PANELS_LIST,
        ALL_AREA_FRAME_LIST
    が基本となる
    """
    def draw_for_routine(
        SURFACE,
        FIELD_PANELS,
        ALL_OTHER_PANELS_LIST,
        ALL_AREA_FRAME_LIST
        ):
        """
        描画に必要なものはこれですべて管理する
        """

        """
        SURFACEの描画
        """
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
                    (panel.position[0] - 3, 
                    panel.position[1] - 3, 
                    panel.size + 6, 
                    panel.size + 6)
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
        for panels in ALL_OTHER_PANELS_LIST:
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

                # こちらが実際のpanel
                pygame.draw.rect(
                    SURFACE, 
                    panel.color, 
                    (panel.position[0], 
                    panel.position[1], 
                    panel.size, 
                    panel.size)
                    )

        """
        AREA_FRAMEの描画
        """
        line_width = 2
        # 枠線の太さ
        for area_frame in ALL_AREA_FRAME_LIST:
            pygame.draw.lines(
                SURFACE,
                area_frame.color,
                True,
                area_frame.vertex_list,
                line_width
            )

    def draw_for_mouse_over_on_field_panels(
        SURFACE,
        FIELD_PANELS,
        ALL_OTHER_PANELS_LIST,
        ALL_AREA_FRAME_LIST,
        mouse_coordinate
    ):
        """
        # mouse_coordinateは、イベントリストから拾ってくるマウスの座標
        # FIELD上の座標ではない。
        # 現在のフィールド上でのユニット名をprintする
        # draw_for_mouse_over_on_panelsで使う
        """
        for row in FIELD_PANELS:
            for panel in row:
                # print("test {}".format(mouse_coordinate))
                if (panel.position[0] < mouse_coordinate[0] < panel.position[0] + panel.size)  \
                    and (panel.position[1] < mouse_coordinate[1] < panel.position[1] + panel.size):
                    # マウスが動かされた場所がpaneleの範囲内なら、その座標をmouse_positionに入れる
                    mouse_coordinate = panel.square.coordinate
                    """
                    ここをコメントインすれば、座標をprintできる
                    """
                    # print(mouse_coordinate)
                    # # for test
                    if panel.square.unit_exist:
                        print(panel.square.unit.name)

    def draw_for_mouse_over_on_other_panels(
        SURFACE,
        FIELD_PANELS,
        ALL_OTHER_PANELS_LIST,
        ALL_AREA_FRAME_LIST,
        mouse_coordinate
    ):
        """
        # mouse_coordinateは、イベントリストから拾ってくるマウスの座標
        # 現在のother_panels上でのユニット名をprintする
        # draw_for_mouse_over_on_panelsで使う
        """
        for panels in ALL_OTHER_PANELS_LIST:
            for panel in panels:
                if (panel.position[0] < mouse_coordinate[0] < panel.position[0] + panel.size)  \
                        and (panel.position[1] < mouse_coordinate[1] < panel.position[1] + panel.size):
                        if panel.flag == True:
                            print(panel.unit.name)

    def draw_for_mouse_over_on_panels(
        SURFACE,
        FIELD_PANELS,
        ALL_OTHER_PANELS_LIST,
        ALL_AREA_FRAME_LIST,
        mouse_coordinate
    ):
        """
        # mouse_coordinateは、イベントリストから拾ってくるマウスの座標
        # FIELD上の座標ではない。
        # 現在のマウスの位置のpanel上のユニット名をprintする
        """
        Drawer.draw_for_mouse_over_on_field_panels(
            SURFACE,
            FIELD_PANELS,
            ALL_OTHER_PANELS_LIST,
            ALL_AREA_FRAME_LIST,
            mouse_coordinate
        )
        Drawer.draw_for_mouse_over_on_other_panels(
            SURFACE,
            FIELD_PANELS,
            ALL_OTHER_PANELS_LIST,
            ALL_AREA_FRAME_LIST,
            mouse_coordinate
        )

    def update_field_panels(FIELD_PANELS):
        """
        # FIELD_PANELのパラメータの更新
        # update_instances_for_drawで使う
        """
        for row in FIELD_PANELS:
            for field_panel in row:
                field_panel.reset_flag()

    def update_other_panels(ALL_OTHER_PANELS_LIST):
        """
        # OTHER_PANELのパラメータの更新
        # update_instances_for_drawで使う
        """
        for other_panels in ALL_OTHER_PANELS_LIST:
            other_panels.reload_panel_unit()
        
    def update_area_frames(ALL_AREA_FRAME_LIST):
        """
        # AREA_FRAMESのパラメータの更新
        # update_instances_for_drawで使う
        """
        for area_frame in ALL_AREA_FRAME_LIST:
            area_frame.change_color_from_occupaied_team()
        # ターンが終わり次第、各AREA_FRAMEの中身をリセットする

    def update_instances_for_draw(
        FIELD_PANELS,
        ALL_OTHER_PANELS_LIST,
        ALL_AREA_FRAME_LIST
    ):
        """
        PANELSとFRAMESのパラメータの更新
        """
        Drawer.update_field_panels(FIELD_PANELS)
        Drawer.update_other_panels(ALL_OTHER_PANELS_LIST)
        Drawer.update_area_frames(ALL_AREA_FRAME_LIST)