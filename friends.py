from cmu_graphics import *
from buttonsClass import *
from PIL import Image


image9 = Image.open('backgrounds/friends.jpg')
image9 = image9.resize((390, 700))
image9 = CMUImage(image9)

def friends_onAppStart(app):
    app.width = 390
    app.height = 700

    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)

def friends_redrawAll(app):
    pilImage = image9.image
    drawImage(image9, 0, 0)

def friends_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
