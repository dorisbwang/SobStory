from cmu_graphics import *
from buttonsClass import *
from PIL import Image


image27 = Image.open('backgrounds/settings.jpg')
image27 = image27.resize((390, 700))
image27 = CMUImage(image27)

def settings_onAppStart(app):
    app.width = 390
    app.height = 700

    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)

def settings_redrawAll(app):
    pilImage = image27.image
    drawImage(image27, 0, 0)

def settings_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
