from cmu_graphics import *
from buttonsClass import *
from sobLogClass import *
from PIL import Image

image6 = Image.open('backgrounds/logSum.jpg')
image6 = image6.resize((390, 700))
image6 = CMUImage(image6)

def logSummary_onAppStart(app):
    app.menuButton = Button('menu', 10, 10, 50, 50)

def logSummary_redrawAll(app):
    pilImage = image6.image
    drawImage(image6, 0, 0)

    drawLabel(app.logClicked.getReason(), 53, 264, fill = 'black')
    drawLabel(app.logClicked.getResolution(), 53, 552, fill = 'black')
    drawLabel(app.logClicked.getDate(), 105, 195)
    drawLabel(app.logClicked.getTime(), 253, 195)



def logSummary_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')



