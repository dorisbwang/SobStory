from cmu_graphics import *
from buttonsClass import *
from PIL import Image

image2 = Image.open('backgrounds/log.jpg')
image2 = image2.resize((390, 700))
image2 = CMUImage(image2)

def sobLog_onAppStart(app):
    app.width = 340
    app.height = 700

    # needs function for text box

    # add button dimensions and placement
    app.menuButton = Button('menu', 0, 0, 50, 50)


def sobLog_redrawAll(app):
    pilImage = image2.image
    drawImage(image2, 0, 0)

def sobLog_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')

