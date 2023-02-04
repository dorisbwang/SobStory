from cmu_graphics import *
from buttonsClass import *
from PIL import Image
from PIL import Image, GifImagePlugin
import sys, os

# Needs: gif of sob bob, screen
# Buttons: log sob, menu

image1 = Image.open('backgrounds/splash.jpg')
image1 = image1.resize((390, 700))
image1 = CMUImage(image1)

def loadAnimatedGif(app, path):
    pilImages = Image.open(path)
    if pilImages.format != 'GIF':
        raise Exception(f'{path} is not an animated image!')
    if not pilImages.is_animated:
        raise Exception(f'{path} is not an animated image!')
    cmuImages = [ ]
    for frame in range(pilImages.n_frames):
        pilImages.seek(frame)
        pilImage = pilImages.copy()
        cmuImages.append(CMUImage(pilImage))
    return cmuImages

def splashScreen_onAppStart(app):
    
    app.width = 390
    app.height = 700
    app.spriteCounter = 0
    bobGif = loadAnimatedGif(app, 'backgrounds/splashScreenGif.gif')
    # add button dimensions and placement
    app.logButton = Button('log', 25, 558, 340, 62)
    app.menuButton = Button('menu', 10, 10, 50, 50)


def splashScreen_redrawAll(app):
    pilImage = image1.image
    drawImage(image1, 0, 0)
    sprite = bobGif[app.spriteCounter]
    drawImage(sprite, 100, 100, align='center')

def splashScreen_onMousePress(app, mouseX, mouseY):
    if app.logButton.buttonPress(mouseX, mouseY):
        # goes to sob log screen
        setActiveScreen('sobLog')
    elif app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')

def splashScreen_onStep(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(bobGif)
