from cmu_graphics import *
from buttonsClass import *
from graphStuff import *
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
    app.arrowButton = Button("arrow", 335, 337, 26, 26)
    app.pieChart = PieChart("Sob Log", 
                            {"School": 2, "Love": 3, "money": 1, "Sad": 3, "work": 6})
    app.monthChart = LineChart("Monthly Sob Log", 
                                {"Jan": 1, "Feb": 2, "Mar": 0, "Apr": 5, "May": 0,
                                "Jun": 0, "Jul": 3, "Aug": 0, "Sep": 4, "Oct": 0,
                                "Nov": 0, "Dec": 7 })

def myStory_redrawAll(app):
    pilImage = image4.image
    drawImage(image4, 0, 0)
    drawCircle(348, 350, 13, fill = None, border = 'black')
    drawLabel(">", 350, 350, size = 25)
    app.pieChart.drawPieChart(130, 200, 170, 170)
    app.monthChart.drawLineChart(40, 400, 300, 200)

def myStory_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
    elif app.arrowButton.buttonPress(mouseX, mouseY):
        print("move right now")
