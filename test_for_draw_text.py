"""
画面上にメッセージを出す
"""


import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN,MOUSEBUTTONUP, MOUSEMOTION

pygame.init()
SURFACE = pygame.display.set_mode((400,200))
FPSCLOCK = pygame.time.Clock()

def main():
    sysfont = pygame.font.SysFont(None, 72)
    lettters = ""
    message = sysfont.render(
        lettters,
        True,
        (0, 128, 128)
        )
    message_rect = message.get_rect()
    message_rect.center = (200, 100)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                lettters = "clicked"
                message = sysfont.render(
                    lettters,
                    True,
                    (0, 128, 128)
                    )
                message_rect.center = event.pos
            elif event.type == MOUSEBUTTONUP:
                lettters = "un_clicked"
                message = sysfont.render(
                    lettters,
                    True,
                    (0, 128, 128)
                    )
                message_rect.center = event.pos
            elif event.type == MOUSEMOTION:
                if event.pos[0] >= 200:    
                    lettters = "moving"
                    message = sysfont.render(
                        lettters,
                        True,
                        (0, 128, 128)
                        )
                    message_rect.center = event.pos
                else:
                    lettters = ""
                    message = sysfont.render(
                        lettters,
                        True,
                        (0, 128, 128)
                        )
                    message_rect.center = event.pos                                    
            else:
                lettters = ""
                message = sysfont.render(
                    lettters,
                    True,
                    (0, 128, 128)
                    )                
        SURFACE.fill((255, 255, 255))
        SURFACE.blit(message, message_rect)
        pygame.display.update()
        FPSCLOCK.tick(300)

if __name__ == "__main__":
    main()