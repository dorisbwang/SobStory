from cmu_graphics import *
from buttonsClass import *
from PIL import Image

image5 = Image.open('backgrounds/resources.jpg')
image5 = image5.resize((390, 700))
image5 = CMUImage(image5)

def resources_onAppStart(app):
    app.width = 340
    app.height = 700

    # needs function for text box

    # add button dimensions and placement
    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)


def resources_redrawAll(app):
    pilImage = image5.image
    drawImage(image5, 0, 0)

def resources_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')