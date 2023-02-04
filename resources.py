from cmu_graphics import *
from buttonsClass import *
from PIL import Image
import webbrowser

image5 = Image.open('backgrounds/resources2.jpg')
image5 = image5.resize((390, 700))
image5 = CMUImage(image5)

def resources_onAppStart(app):
    app.width = 390
    app.height = 700

    # needs function for text box

    # add button dimensions and placement
    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)
    app.headspaceButton = Button("headspace", 22, 130, 160, 160)
    app.timelycareButton = Button("timelycare", 207, 127, 160, 160)
    app.upbeatSpotifyButton = Button("upbeat", 22, 312, 160, 160)
    app.discoButton = Button("disco", 207, 312, 160, 160)
    app.icecreamButton = Button("ice cream", 22, 497, 160, 160)
    app.dogButton = Button("dog", 207, 497, 160, 160)


def resources_redrawAll(app):
    pilImage = image5.image
    drawImage(image5, 0, 0)

def resources_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
    elif app.headspaceButton.buttonPress(mouseX, mouseY):
        webbrowser.open('https://www.headspace.com/', new=2)
    elif app.timelycareButton.buttonPress(mouseX, mouseY):
        webbrowser.open("https://timely.md/support/", new=2)
    elif app.upbeatSpotifyButton.buttonPress(mouseX, mouseY):
        webbrowser.open("https://open.spotify.com/playlist/1LcNuLsbK6T2Swwum9D9NS?si=cc5b395f93d84e18&nd=1", new = 2)
    elif app.discoButton.buttonPress(mouseX, mouseY):
        print("disco")
        # setActiveScreen("disco") #make a disco screen
    elif app.icecreamButton.buttonPress(mouseX, mouseY):
        webbrowser.open("https://www.google.com/search?q=ice+cream+near+me&oq=ice+cream+near+me&aqs=chrome..69i57j0i402l2j0i512l7.50427j1j9&sourceid=chrome&ie=UTF-8", new = 2)
    elif app.dogButton.buttonPress(mouseX, mouseY):
        webbrowser.open("https://www.google.com/search?q=dog+pictures&oq=dog+pictures&aqs=chrome..69i57j0i433i512j0i512l5j69i61.3548j0j9&sourceid=chrome&ie=UTF-8", new = 2)