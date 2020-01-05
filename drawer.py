import sys
import pygame
from pygame.locals import  QUIT, Rect, MOUSEBUTTONDOWN

import game_initilizer

class Panel:
    color_none = (255, 255, 255)
    # いないのはwhite
    color_exist = (0, 0, 0)
    # いるのはblack

    def __init__(self, position: list, size: int):
        self.position = position
        self.size = size
        self.flag = False
        self.color = Panel.color_none
        self.square = None

    def make_flag_change(self):
        """
        flagを反転させて、colorプロパティを変える
        """
        self.flag = not self.flag
        if self.flag == True:
            self.color = Panel.color_exist
        else:
            self.color = Panel.color_none

    def get_square(self, square):
        self.square = square

    def flag_reset(self):
        """
        unit.existがTrueなら、flagをTrueにして描画させる
        """
        self.flag = self.square.unit_exist
        # print("flag.reset is called")
        if self.flag == True:
            self.color = Panel.color_exist
        else:
            self.color = Panel.color_none
