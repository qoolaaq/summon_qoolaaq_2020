import sys
import pygame
from pygame.locals import  QUIT

pygame.init()
# pygameを使うアプリでは必ず最初に呼び出す必要がある
SURFACE = pygame.display.set_mode((400,300))
# サイズを指定してウィンドウを表示
# 引数は(width, height)
pygame.display.set_caption("Just Window")
# ウィンドウのタイトル
FPSCLOCK = pygame.time.Clock()
# クロックオブジェクトを作り、変数をFPSCLOCKに格納する

def main():
    """main routine"""
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0

    while True:
        for event in pygame.event.get(QUIT):
        # イベントキューからイベントを取得する
            pygame.quit()
            sys.exit()

        counter += 1

        SURFACE.fill((0,0,0))
        # SURFACEの中身をタプル()で塗りつぶす
        # (R,G,B)
        # (255,255,255)で白
        count_image = sysfont.render("count is {}".format(counter), True, (255, 255, 255))
        SURFACE.blit(count_image, (50,50))
        pygame.display.update()
        # プログラム内で描画した内容を反映させる
        FPSCLOCK.tick(10)
        # 1秒間に10回ループを回す

if __name__ == "__main__":
    main()

