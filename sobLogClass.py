from cmu_graphics import *
from dataAnalysis import *
import math
import copy

class SobLog():
    logs = []

    def __init__ (self, date, time, reason, resolution):
        self.date = date
        self.time = time
        self.reason = reason
        self.resolution = resolution

        SobLog.logs.append(self)
        for log in SobLog.logs:
            dateAnalysis(log.date)
            reasonAnalysis(log.reason)

    
    def getDate(self):
        return self.date
    def getReason(self):
        return self.reason
    
    @staticmethod
    def doDateAnalysis(self):
        for log in SobLog.logs:
            dateAnalysis(log.date)
            return monthlyCryLog
    def doReasonAnalysis(self):
        for log in SobLog.logs:
            reasonAnalysis(log.reason)
            return reasonLog
    
def dateAnalysis(date):
        slash = date.find("/")
        month = date[0:slash]

        i = 0
        for m in monthlyCryLog:
            if i == month:
                monthlyCryLog[m] = monthlyCryLog[m] + 1
            i += 1

def reasonAnalysis(log):
    for reason in reasonsKeyWords:
        for keyword in reasonsKeyWords[reason]:
            if keyword in log:
                    reasonLog[reason] = reasonLog.get(reason, 0) +  1

monthlyCryLog = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0,
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0,
                "Nov": 0, "Dec": 0 }

reasonLog = {"School": 2, "Money":3, "Health": 1, "Relationship": 4}

reasonsKeyWords = {"relationship": ["relationship", "heartbreak", "boyfriend", "girlfriend", "love", "kiss", "date", "breakup", "divorce"],
            "school": ["math", "class", "school", "grades", "exams", "concepts", "computer science"],
            "family": ["mom", "dad", "brother", "sister", "family", "house", "grandma", "grandpa"],
            "money" : ["payment", "money", "dollars", "debt", "broke"],
            "health" : ["cancer", "health", "sick", "terminal", "death depression"],
            "work" : ["boss", "job", "coworker", "businness","work"],
                    }
print(reasonLog)




