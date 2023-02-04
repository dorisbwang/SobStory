from cmu_graphics import *
from buttonsClass import *
 
# Needs: gif of sob bob, screen
# Buttons: log sob, menu

def splashScreen_onScreenStart(app):
    app.top = 0
    app.left = 0
    app.width = 340
    app.height = 844
    # add button dimensions and placement
    app.logButton = Button()
    app.menuButton = Button()

def splashScreen_redrawAll(app):
    drawRect(0, 0, 150, 40, fill = 'yellow', border = 'black')

def onMousePress(mouseX, mouseY):
    if app.logButton.buttonPress(mouseX, mouseY):
        # goes to sob log screen
        setActiveScreen('sobLog')
    elif app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
