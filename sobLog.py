from cmu_graphics import *
from buttonsClass import *
from sobLogClass import *
from PIL import Image

image2 = Image.open('backgrounds/log-page-001.jpg')
image2 = image2.resize((390, 700))
image2 = CMUImage(image2)

def sobLog_onAppStart(app):
    app.width = 340
    app.height = 700

    app.isTypingReason = False
    app.isTypingResolution = False
    app.isTypingDate = False
    app.isTypingTime = False
    app.reasonInput = ""
    app.resolutionInput = ""
    app.dateInput = ""
    app.timeInput = ""
    app.reasonFormat = ""
    app.resolutionFormat = ""
    app.dateFormat = ""
    app.timeFormat = ""
    # needs function for text box

    # add button dimensions and placement
    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.logEndButton = Button("log", 330, 13, 45, 45)
    app.reasonButton = Button("reason", 48, 260, 293, 207)
    app.resolutionButton = Button("resolution", 48, 547, 293, 116)
    app.dateButton = Button("date", 105, 195, 76, 30)
    app.timeButton = Button("time", 253, 195, 70, 30)


def sobLog_redrawAll(app):
    pilImage = image2.image
    drawImage(image2, 0, 0)

    if app.isTypingReason == True:
        drawCircle(315, 440, 12, fill = 'midnightblue')
    elif app.isTypingResolution == True:
        drawCircle(315, 640, 12, fill = 'midnightblue')
    elif app.isTypingDate == True:
        drawCircle(37, 195, 5, fill = 'white')
    elif app.isTypingTime == True:
        drawCircle(187, 195, 5, fill = 'white')

    drawReasonResolution(app.reasonInput) #call the function once for reason and once for resolution textbox
    drawReasonResolution(app.resolutionInput)
    # drawLabel(app.reasonInput, 60, 270, align = "left", font = "monospace") #38 char in a line
    drawDateResolution(app.dateInput)
    drawTimeResolution(app.timeInput)

def drawReasonResolution(inputStr):
    resultList = formatReasonResolution(inputStr)
    if inputStr == app.reasonInput:
        startY = 270
    elif inputStr == app.resolutionInput:
        startY = 558

    for i in range(len(resultList)):
        drawLabel(resultList[i], 60, startY+(12*i), align = "left", font = "monospace")
def drawDateResolution(inputStr):
    resultList = formatReasonResolution(inputStr)
    if inputStr == app.dateInput:
        startY = 195
    for i in range(len(resultList)):
        drawLabel(resultList[i], 105, startY+(12*i), align = "left", font = "monospace", fill = "white", bold = True)
def drawTimeResolution(inputStr):
    resultList = formatReasonResolution(inputStr)
    if inputStr == app.timeInput:
        startY = 195
    for i in range(len(resultList)):
        drawLabel(resultList[i], 253, startY+(12*i), align = "left", font = "monospace", fill = "white", bold = True)

def formatReasonResolution(inputStr):
    resultList = [""] #list with str for each line of the textbox

    #format into a local list
    inputList = inputStr.split(" ")
    maxLength = 38
    numLines = 0
    if inputStr == app.reasonInput:
      maxLines = 16
    elif inputStr == app.resolutionInput:
      maxLines = 9
    elif inputStr == app.dateInput:
      maxLines = 1
    elif inputStr == app.timeInput:
      maxLines = 1
    while inputList != []:
        #the max number of lines stuff doesnt work so i will try to
        # fix this tomorrow if there is time because this is a small detail
        if (maxLines - 2) < numLines <= (maxLines - 1):
            maxLength = 32
        elif numLines > maxLines - 1:
            if inputStr == app.resolutionInput:
                drawRect(300, 625, 30, 30, fill = "red")
            elif inputStr == app.reasonInput:
                drawRect(300, 425, 30, 30, fill = "red")
            elif inputStr == app.dateInput:
                drawRect(175, 189, 14, 14, fill = "red")
            break
        if len(resultList[numLines]) + len(inputList[0]) <= maxLength:
            resultList[numLines] += inputList[0] + " "
            inputList.pop(0)
        else:
            numLines += 1
            resultList.append("")
            resultList[numLines] = inputList[0] + " "
            inputList.pop(0)
    return resultList


def sobLog_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.reasonButton.buttonPress(mouseX, mouseY):
        #toggles for the reason explanation
        if app.isTypingReason == False:
            app.isTypingReason = True
            app.isTypingResolution = False
            app.isTypingTime = False
            app.isTypingDate = False
            #start typing reason
            pass
        else:
            app.isTypingReason = False
    elif app.resolutionButton.buttonPress(mouseX, mouseY):
        #toggles for the resolution explanation
        if app.isTypingResolution == False:
            app.isTypingResolution = True
            app.isTypingReason = False
            app.isTypingTime = False
            app.isTypingDate = False
            #start typing reason
            pass
        else:
            app.isTypingResolution = False
    elif app.dateButton.buttonPress(mouseX, mouseY):
        #toggles for the resolution explanation
        if app.isTypingDate == False:
            app.isTypingDate = True
            app.isTypingResolution = False
            app.isTypingTime = False
            app.isTypingReason = False
            #start typing date
            pass
        else:
            app.isTypingDate = False
    elif app.timeButton.buttonPress(mouseX, mouseY):
        #toggles for the resolution explanation
        if app.isTypingTime == False:
            app.isTypingTime = True
            app.isTypingDate = False
            app.isTypingResolution = False
            app.isTypingReason = False
            #start typing date
            pass
        else:
            app.isTypingTime = False
    elif app.logEndButton.buttonPress(mouseX, mouseY):
        print("ASHFJKAHKLJS")
        #############################################DORIS
        app.currLog = SobLog(app.dateFormat, app.timeFormat, app.reasonFormat, app.resolutionFormat)
        app.reasonInput = ""
        app.resolutionInput = ""
        app.dateInput = ""
        app.timeInput = ""
        app.reasonFormat = ""
        app.resolutionFormat = ""
        app.dateFormat = ""
        app.timeFormat = ""

        print(SobLog.logs)
        setActiveScreen('resources')



def sobLog_onKeyPress(app, key):
    if app.isTypingReason:
        app.reasonInput = inputMessage(app, key, app.reasonInput)
    elif app.isTypingResolution:
        app.resolutionInput = inputMessage(app, key, app.resolutionInput)
    elif app.isTypingDate:
        app.dateInput = inputMessage(app, key, app.dateInput)
    elif app.isTypingTime:
        app.timeInput = inputMessage(app, key, app.timeInput)

def inputMessage(app, key, input):
    if key == "backspace":
        input = input[:-1]
    elif key == "space":
        input = input + " "
    elif key == "enter":
        app.isTypingReason = False
        app.isTypingResolution = False
        app.isTypingDate = False
        app.isTypingTime = False
    else:
        input = input + str(key)
    return input

