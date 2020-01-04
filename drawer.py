import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

import game_initilizer

pygame.init()
# pygameを使うアプリでは必ず最初に呼び出す必要がある
WIDTH = 640
HEIGHT = 360
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
# サイズを指定してウィンドウを表示
# 引数は(WIDTH, HEIGHT)
pygame.display.set_caption("summon_qoolaaq")
# ウィンドウのタイトル
FPSCLOCK = pygame.time.Clock()
# クロックオブジェクトを作り、変数をFPSCLOCKに格納する

SQUARE_SIZE = 50

class Square:
    color_none = (255, 255, 255)
    # いないのはwhite
    color_exist = (0, 0, 0)
    # いるのはblack

    def __init__(self, position: list, flag: bool):
        self.position = position
        self.size = SQUARE_SIZE
        self.flag = flag
        self.color = Square.color_none
    
    def make_flag_change(self):
        self.flag = not self.flag
        if self.flag == True:
            self.color = Square.color_exist
        else:
            self.color = Square.color_none

FIELD = []
FIELD = [[Square([30 + i * 60, 30 + j * 60], False) for i in range(5)] for j in range(5)]

def main():
    """main routine"""
    sysfont = pygame.font.SysFont(None, 50)
    mousepos = []
    # ここにマウスがクリックされたときの座標情報がタプルとして入る

    while True:
        SURFACE.fill((128, 128, 128))
        # SURFACEの中身をタプル()で塗りつぶす
        # (R,G,B)
        # (255,255,255)で白

        """
        5*5のマスを表示させる。
        """
        
        # for i in range(5):
        #     for j in range(5):
        #         FIELD = [[Square([30 + i * 60, 30 + j * 60])]]
        #         # pygame.draw.rect(SURFACE, (255, 255, 255), (30 + i * 60, 30 + j * 60, 50, 50))
        
        for row in FIELD:
            for square in row:
                pygame.draw.rect(SURFACE, square.color, (square.position[0], square.position[1], square.size, square.size))
                # square.position -> [xpos, ypos]

        for event in pygame.event.get():
        # イベントキューからイベントを取得する
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)
                # マウスの座標＝event.posでタプルとして取得
                for row in FIELD:
                    for square in row:
                        # print("test {}".format(event.pos))
                        if (square.position[0] < event.pos[0] < square.position[0] + square.size)  \
                            and (square.position[1] < event.pos[1] < square.position[1] + square.size):
                            # クリックされた場所がsquareの範囲内なら、そのsquareのmake_flag_changeを行う
                            square.make_flag_change()

        """
        mouseposから座標の情報を引っ張ってきて、円を描写
        """
        # for i, j in mousepos:
        #     pygame.draw.circle(SURFACE, (0, 255, 0), (i, j), 5)
        #     print(mousepos)

        # for xpos in range(0, 400, 25):
        #     pygame.draw.line(SURFACE, 0xFFFFF, (xpos, 0), (xpos, 300))
        #     # (SURFACE, 色(0xFFFFF), 始点(xpos, ypos), 終点(xpos, ypos))
        
        # for ypos in range(0, 300, 25):
        #     pygame.draw.line(SURFACE, 0xFFFFF, (0, ypos), (400, ypos))
        #     # (SURFACE, 色(0xFFFFF), 始点(xpos, ypos), 終点(xpos, ypos))

        pygame.display.update()
        # プログラム内で描画した内容を反映させる
        FPSCLOCK.tick(10)
        # 1秒間に10回ループを回す

if __name__ == "__main__":
    main()
