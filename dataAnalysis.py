from sobLogClass import *

monthlyCryLog = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0,
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0,
                "Nov": 0, "Dec": 0 }
reasonLog = dict()

reasonsKeyWords = {"relationship": ["relationship", "heartbreak", "boyfriend", "girlfriend", "love", "kiss", "date", "breakup", "divorce"],
            "school": ["math", "class", "school", "grades", "exams", "concepts", "computer science"],
            "family": ["mom", "dad", "brother", "sister", "family", "house", "grandma", "grandpa"],
            "money" : ["payment", "money", "dollars", "debt", "broke"],
            "health" : ["cancer", "health", "sick", "terminal", "death depression"],
            "work" : ["boss", "job", "coworker", "businness","work"],
                    }