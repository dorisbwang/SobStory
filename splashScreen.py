from cmu_graphics import *
from buttonsClass import *
from PIL import Image

# Needs: gif of sob bob, screen
# Buttons: log sob, menu

image1 = Image.open('backgrounds/splash.jpg')
image1 = image1.resize((390, 700))
image1 = CMUImage(image1)


def splashScreen_onAppStart(app):
    app.width = 390
    app.height = 700

    # add button dimensions and placement
    app.logButton = Button('log', 25, 558, 340, 62)
    app.menuButton = Button('menu', 0, 0, 50, 50)

def splashScreen_redrawAll(app):
    pilImage = image1.image
    drawImage(image1, 0, 0)

def splashScreen_onMousePress(app, mouseX, mouseY):
    if app.logButton.buttonPress(mouseX, mouseY):
        # goes to sob log screen
        setActiveScreen('sobLog')
    elif app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
