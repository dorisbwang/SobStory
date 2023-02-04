from cmu_graphics import *
from buttonsClass import *
from PIL import Image
from PIL import Image, GifImagePlugin
from PIL import Image, ImageSequence
import sys, os
import webbrowser

image5 = Image.open('backgrounds/resources2.jpg')
image5 = image5.resize((390, 700))
image5 = CMUImage(image5)

def resources_onAppStart(app):
    app.isDisco = False

    app.width = 390
    app.height = 700

    # add button dimensions and placement
    app.menuButton = Button('menu', 10, 10, 50, 50)
    app.soblogButton = Button("sob log", 309, 10, 75, 53)
    app.headspaceButton = Button("headspace", 22, 130, 160, 160)
    app.timelycareButton = Button("timelycare", 207, 127, 160, 160)
    app.upbeatSpotifyButton = Button("upbeat", 22, 312, 160, 160)
    app.discoButton = Button("disco", 207, 312, 160, 160)
    app.icecreamButton = Button("ice cream", 22, 497, 160, 160)
    app.dogButton = Button("dog", 207, 497, 160, 160)
    app.discoOff = Button("discoOff", 22, 210, 346, 367)

    appDisco(app)

def appDisco(app):
    app.stepsPerSecond = 4
    app.spriteCounter1 = 0
    app.bobDance = loadAnimatedGif(app, 'backgrounds/bobDance.gif')
    app.discoColor = ["darkViolet", "yellow", "fuchsia", "lime", "red", "blue"]
    app.colorCount = 0


def resources_redrawAll(app):
    pilImage = image5.image
    drawImage(image5, 0, 0)
    if app.isDisco:
        drawDisco(app)

def drawDisco(app):
    drawRect(22, 210, 346, 367)

    #draw disco lights
    print(app.discoColor[app.colorCount])
    drawCircle(195, 240, 30, fill = app.discoColor[app.colorCount])
    drawLine(177, 244, 22, 314, fill = app.discoColor[app.colorCount], lineWidth = 10)
    drawLine(23, 431, 184, 254, fill = app.discoColor[app.colorCount], lineWidth = 10)
    drawLine(195, 258, 137, 577, fill = app.discoColor[app.colorCount], lineWidth = 10)
    drawLine(327, 577, 204, 255, fill = app.discoColor[app.colorCount], lineWidth = 10)
    drawLine(210, 242, 368, 343, fill = app.discoColor[app.colorCount], lineWidth = 10)


    sprite = app.bobDance[app.spriteCounter1]
    drawImage(sprite, 195, 480, align='center')

def resources_onStep(app):
    app.spriteCounter1 = (1 + app.spriteCounter1) % len(app.bobDance)
    app.colorCount = (app.colorCount + 1)%6

def resources_onMousePress(app, mouseX, mouseY):
    if app.menuButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('menu')
    elif app.soblogButton.buttonPress(mouseX, mouseY):
        # goes to menu screen
        setActiveScreen('sobLog')
    if app.isDisco == False:
        if app.headspaceButton.buttonPress(mouseX, mouseY):
            webbrowser.open('https://www.headspace.com/about-us', new=2)
        elif app.timelycareButton.buttonPress(mouseX, mouseY):
            webbrowser.open("https://timely.md/support/", new=2)
        elif app.upbeatSpotifyButton.buttonPress(mouseX, mouseY):
            webbrowser.open("https://open.spotify.com/playlist/1LcNuLsbK6T2Swwum9D9NS?si=cc5b395f93d84e18&nd=1", new = 2)
        elif app.discoButton.buttonPress(mouseX, mouseY):
            print("disco")
            app.isDisco = True
        elif app.icecreamButton.buttonPress(mouseX, mouseY):
            webbrowser.open("https://www.google.com/search?q=ice+cream+near+me&oq=ice+cream+near+me&aqs=chrome..69i57j0i402l2j0i512l7.50427j1j9&sourceid=chrome&ie=UTF-8", new = 2)
        elif app.dogButton.buttonPress(mouseX, mouseY):
            webbrowser.open("https://www.google.com/search?q=dog+pictures&oq=dog+pictures&aqs=chrome..69i57j0i433i512j0i512l5j69i61.3548j0j9&sourceid=chrome&ie=UTF-8", new = 2)
    else:
        if app.discoOff.buttonPress(mouseX, mouseY):
            app.isDisco = False

def loadAnimatedGif(app, path):
    pilImages = Image.open(path)
    if pilImages.format != 'GIF':
        raise Exception(f'{path} is not an animated image!')
    if not pilImages.is_animated:
        raise Exception(f'{path} is not an animated image!')
    cmuImages = [ ]
    for frame in range(pilImages.n_frames):
        pilImages.seek(frame)
        pilImage = pilImages.copy()
        cmuImages.append(CMUImage(pilImage))
    return cmuImages