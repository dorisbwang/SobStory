from cmu_graphics import *
from buttonsClass import *
from PIL import Image

image3 = Image.open('backgrounds/menu.jpg')
image3 = image3.resize((390, 700))
image3 = CMUImage(image3)

def menu_onAppStart(app):
    app.width = 340
    app.height = 700

    # needs function for text box

    # add button dimensions and placement
    app.soblogButton = Button("sob log", 309, 10, 75, 53)
    app.sobstoryButton = Button('sob story', 48, 214, 293, 60)
    # app.friendsButton = Button('friends', 48, 307, 293, 60) 
    # app.musicButton = Button('music', 48, 399, 293, 60)
    app.resourcesButton = Button('rec', 48, 492, 293, 60)
    


def menu_redrawAll(app):
    pilImage = image3.image
    drawImage(image3, 0, 0)

def menu_onMousePress(app, mouseX, mouseY):
    if app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
    elif app.sobstoryButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('myStory')
    elif app.resourcesButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('resources')