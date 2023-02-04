from cmu_graphics import *
from buttonsClass import *
from PIL import Image

def sobLog_onScreenStart(app):
    app.top = 0
    app.left = 0
    app.width = 340
    app.height = 844
    #background
    app.image = Image.open('backgrounds/splash.jpg')
    app.image = CMUImage(app.image)

    # add button dimensions and placement
    app.logButton = Button()
    app.menuButton = Button()

def sobLog_redrawAll(app):
    pilImage = app.image.image
    drawImage(app.image, 500, 200, align='center',
              width=pilImage.width//2,
              height=pilImage.height//2)

def sobLog_onMousePress(mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')

