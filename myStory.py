from cmu_graphics import *
from buttonsClass import *
from PIL import Image

image4 = Image.open('backgrounds/myStory.jpg')
image4 = image4.resize((390, 700))
image4 = CMUImage(image4)

def myStory_onAppStart(app):
    app.width = 390
    app.height = 700

    # needs function for text box

    # add button dimensions and placement
    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)


def myStory_redrawAll(app):
    pilImage = image4.image
    drawImage(image4, 0, 0)

def myStory_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
