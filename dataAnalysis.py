
monthlyCryLog = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0,
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0,
                "Nov": 0, "Dec": 0 }
reasonLog = dict()

reasons = {"love": "heartbreak, boyfriend, girlfriend, love, kiss, date, breakup, divorce, "
                    }

def dateAnalysis(dateList):
    for date in dateList:
        slash = date.find("/")
        month = date[0:slash]

        i = 0
        for m in monthlyCryLog:
            if i == month:
                monthlyCryLog[m] = monthlyCryLog[m] + 1
            i += 1

def reasonAnalysis(reasons):
    pass
