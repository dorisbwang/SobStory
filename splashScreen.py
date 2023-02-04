from cmu_graphics import *
from buttonsClass import *
from PIL import Image
 
# Needs: gif of sob bob, screen
# Buttons: log sob, menu

image1 = Image.open('backgrounds/splash.jpg')
image1 = CMUImage(image1)

def splashScreen_onAppStart(app):
    app.width = 340
    app.height = 700
    # background
    # app.image1 = Image.open('backgrounds/splash.jpg')
    # app.image1 = CMUImage(app.image1)
    # add button dimensions and placement
    # app.logButton = Button()
    # app.menuButton = Button()

def splashScreen_redrawAll(app):
    pilImage = image1.image
    drawImage(image1, 500, 200, align='center')

def splashScreen_onMousePress(mouseX, mouseY):
    if app.logButton.buttonPress(mouseX, mouseY):
        # goes to sob log screen
        setActiveScreen('sobLog')
    elif app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')