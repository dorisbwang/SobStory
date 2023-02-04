from cmu_graphics import *
import math
import copy

class SobLog():
    def __init__ (self, date, time, reason, resolution):
        self.date = date
        self.time = time
        self.reason = reason
        self.resolution = resolution