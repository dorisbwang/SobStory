from cmu_graphics import *
from PIL import Image

from splashScreen import *
from sobLog import *
from myStory import *
from menu import *
from resources import *
from friends import *
from settings import *

import sys, os

def main():
    runAppWithScreens(initialScreen='splashScreen', width = 390, height = 700)
main()
