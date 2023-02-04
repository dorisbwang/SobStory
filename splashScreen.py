from cmu_graphics import *
from buttonsClass import *
from PIL import Image
 
# Needs: gif of sob bob, screen
# Buttons: log sob, menu

def splashScreen_onAppStart(app):
    app.width = 340
    app.height = 844
    # background
    app.image1 = Image.open('backgrounds/splash.jpg')
    app.image1 = CMUImage(app.image1)
    # add button dimensions and placement
    app.logButton = Button()
    app.menuButton = Button()

def splashScreen_redrawAll(app):
    pilImage = app.image1.image
    drawImage(app.image1, 500, 200, align='center',
              width=pilImage.width//2,
              height=pilImage.height//2)

def splashScreen_onMousePress(mouseX, mouseY):
    if app.logButton.buttonPress(mouseX, mouseY):
        # goes to sob log screen
        setActiveScreen('sobLog')
    elif app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')

from tkinter import *

root = Tk()
root.geometry("200x200")

textBox = Text(root, width = 60, height = 40)
textBox.pack(pady = 10)
