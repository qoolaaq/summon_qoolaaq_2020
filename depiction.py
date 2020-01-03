import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

pygame.init()
# pygameを使うアプリでは必ず最初に呼び出す必要がある
WIDTH = 400
HEIGHT = 300
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
# サイズを指定してウィンドウを表示
# 引数は(WIDTH, HEIGHT)
pygame.display.set_caption("Just Window")
# ウィンドウのタイトル
FPSCLOCK = pygame.time.Clock()
# クロックオブジェクトを作り、変数をFPSCLOCKに格納する

def main():
    """main routine"""
    sysfont = pygame.font.SysFont(None, 50)
    mousepos = []
    # ここにマウスがクリックされたときの座標情報がタプルとして入る

    while True:
        SURFACE.fill((255, 255, 255))
        # SURFACEの中身をタプル()で塗りつぶす
        # (R,G,B)
        # (255,255,255)で白

        for event in pygame.event.get():
        # イベントキューからイベントを取得する
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)
                # マウスの座標＝event.posでタプルとして取得

        for i, j in mousepos:
            pygame.draw.circle(SURFACE, (0, 255, 0), (i, j), 5)
        # mouseposから座標の情報を引っ張ってきて、円を描写

        for xpos in range(0, 400, 25):
            pygame.draw.line(SURFACE, 0xFFFFF, (xpos, 0), (xpos, 300))
            # (SURFACE, 色(0xFFFFF), 始点(xpos, ypos), 終点(xpos, ypos))
        
        for ypos in range(0, 300, 25):
            pygame.draw.line(SURFACE, 0xFFFFF, (0, ypos), (400, ypos))
            # (SURFACE, 色(0xFFFFF), 始点(xpos, ypos), 終点(xpos, ypos))

        pygame.display.update()
        # プログラム内で描画した内容を反映させる
        FPSCLOCK.tick(10)
        # 1秒間に10回ループを回す

if __name__ == "__main__":
    main()

