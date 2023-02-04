from cmu_graphics import *
import math

class PieChart(): 
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.colors = [ rgb(255,241,200), rgb(247,184,162), rgb(234,95,137),
                        rgb(155,50,146), rgb(87, 23, 126), rgb(42,11,163)]

        #take into account the size of the labels on the side
    def drawPieChart(self, x, y, width, height):
        drawLabel(f'{self.name}', x + width/2, y - height/2 - 20, size = 16,
                    bold = True)
        percents = self.getPercentage()
        startAngle = 0
        i = 0
        for label in self.data:
                percent = percents[i]
                if percent > 0:
                        sweepAngle = 360*percent/100
                        drawArc(x, y, width, height, startAngle, sweepAngle,
                        fill = self.colors[i%(len(self.colors)-1)])
                        startAngle += sweepAngle
                drawLabel(f'{label}: {rounded(percent)}%', x + width - 30, y - 30 + 20*i, 
                            align = "left")
                drawCircle(x + width - 40, y - 30 + 20*i, 5, 
                            fill = self.colors[i%(len(self.colors)-1)])
                i += 1
    
    def getPercentage(self):
        total = 0
        for label in self.data:
                total += self.data[label]
        percents = [100* self.data[label]/total for label in self.data]
        return percents

class LineChart(): 
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.color = rgb(234,95,137)

        #take into account the size of the labels on the side
    def drawLineChart(self, x, y, width, height):
        drawLabel(f'{self.name}', x + width/2, y - 20, size = 16,
                    bold = True)
        i = 0
        maxP = self.getMaxDataPoint()
        #the interval in between points
        interval = height/maxP
        drawLine(x,y - 10,x,y+height)
        drawLine(x,y+height, x+width, y+height)
        for label in self.data:
                if self.data[label] > 0:
                    drawCircle(10 + i*width/12+x, y + height - self.data[label]*interval, 5,
                    fill = rgb(87, 23, 126))
                drawLabel(f'{label}', 10 + i*width/12+x, y + height + 10)
                i += 1
        for j in range(maxP+1):
            drawLabel(f'{j}', x - 10,  y + height - j*interval)
    
    def getMaxDataPoint(self):
        maxP = 0
        for label in self.data:
            if self.data[label] > maxP: maxP = self.data[label]
        return maxP+1
