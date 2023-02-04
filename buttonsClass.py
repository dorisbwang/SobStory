from cmu_graphics import *
import math
import copy

class Button(): 
    def __init__(self, name, left, top, width, height):
        self.name = name
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def buttonPress(self, x, y):
        if self.left <= x <= self.left + self.width and self.top <= y <= self.top + self.height:
            return True
        return False