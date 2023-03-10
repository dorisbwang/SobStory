from cmu_graphics import *
from dataAnalysis import *
import math
import copy

class SobLog():
    logs = []
    monthlyCryLog = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0,
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0,
                "Nov": 0, "Dec": 0 }

    reasonLog = {"school": 0, "money":0, "health": 0, "relationship": 0, "work": 0}

    def __init__ (self, date, time, reason, resolution):
        self.date = date
        self.time = time
        self.reason = reason
        self.resolution = resolution

        SobLog.logs.append(self)


    def getDate(self):
        return self.date
    def getReason(self):
        return self.reason

    @staticmethod
    def doDateAnalysis():
        for log in SobLog.logs:
            SobLog.dateAnalysis(log.date)
        return SobLog.monthlyCryLog
    @staticmethod
    def doReasonAnalysis():
        for log in SobLog.logs:
            SobLog.reasonAnalysis(log.reason)
        return SobLog.reasonLog

    @staticmethod
    def dateAnalysis(date):
        slash = date.find("/")
        month = date[0:slash]

        i = 1
        print(date, "date")
        for m in SobLog.monthlyCryLog:
            if i == int(month):
                SobLog.monthlyCryLog[m] = SobLog.monthlyCryLog[m] + 1
            i += 1
    @staticmethod
    def reasonAnalysis(log):
        for reason in reasonsKeyWords:
            for keyword in reasonsKeyWords[reason]:
                print(log, "111111log")
                if keyword in log:
                    SobLog.reasonLog[reason] = SobLog.reasonLog.get(reason, 0) +  1


reasonsKeyWords = {"relationship": ["relationship", "heartbreak", "boyfriend", "girlfriend", "love", "kiss", "date", "breakup", "divorce"],
            "school": ["math", "class", "school", "grades", "exams", "concepts", "computer science", "homework"],
            "family": ["mom", "dad", "brother", "sister", "family", "house", "grandma", "grandpa"],
            "money" : ["payment", "money", "dollars", "debt", "broke"],
            "health" : ["cancer", "health", "sick", "terminal", "death depression"],
            "work" : ["boss", "job", "coworker", "businness","work"],
                    }





