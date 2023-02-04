from cmu_graphics import *
from buttonsClass import *
from sobLogClass import *
from PIL import Image

image6 = Image.open('backgrounds/myLog.jpg')
image6 = image6.resize((390, 700))
image6 = CMUImage(image6)

def myLog_onAppStart(app):
    app.width = 390
    app.height = 700

    # add button dimensions and placement
    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)

    if len(SobLog.logs) > 0:
        if len(SobLog.logs) >= 5:
            app.sobLogsShown = SobLog.logs[(len(SobLog.logs) - 5): len(SobLog.logs)]
            app.sobLogsShown.reverse()
            print("THIS IS SHOWN", app.sobLogsShown)
        else:
            app.sobLogsShown = reversed(SobLog.logs)

def myLog_redrawAll(app):
    pilImage = image6.image
    drawImage(image6, 0, 0)
    print(SobLog.logs)

    if len(SobLog.logs) > 0:
        print('AWFJHKA')
        for i in range(len(app.sobLogsShown)):
            logNum = len(SobLog.logs) - i
            drawLabel(f'LOG {logNum}', 194, 187 + i * 93, align = 'center', size = 20, fill = rgb(205, 228, 255))

def myLog_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')