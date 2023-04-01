import json
import random

# with open('users.json') as a:
#     data = json.load(a)
    

class User:
    def __init__(self,
                username:str=None,
                timeSlept:int=0,
                timeStopSleep:int=0,
                weekSum:int=0,
                sleepDate:int=0,
                wakeUpDate:int=0,
                monday:int=0,
                tuesday:int=0,
                wednesday:int=0,
                thursday:int=0,
                friday:int=0,
                saturday:int=0,
                sunday:int=0,
                today:int=0):
        self.username = username
        self.timeSlept = timeSlept
        self.timeStopSleep = timeStopSleep
        self.weekSum = weekSum
        self.sleepDate = sleepDate
        self.wakeUpDate = wakeUpDate
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.today = today

    def sleepCount(self):
        return self.timeStopSleep - self.timeSlept if self.wakeUpDate == self.sleepDate else 24 - self.timeSlept + self.timeStopSleep
    
    def amountSleptCompare(self): 
        if(self.today == 1):
            return self.monday - self.sunday
        elif(self.today == 2):
            return self.tuesday - self.monday
        elif(self.today == 3):
            return self.wednesday - self.tuesday
        elif(self.today == 4):
            return self.thursday - self.wednesday
        elif(self.today == 5):
            return self.friday - self.thursday
        elif(self.today == 6):
            return self.saturday - self.friday
        elif(self.today == 7):
            return self.sunday - self.saturday
    
    def todaySleep(self): #call once a day
        self.weekSum += self.sleepCount()
        if(self.today == 1):
            self.monday = self.sleepCount()
        elif(self.today == 2):
            self.tuesday = self.sleepCount()
        elif(self.today == 3):
            self.wednesday = self.sleepCount()
        elif(self.today == 4):
            self.thursday = self.sleepCount()
        elif(self.today == 5):
            self.friday = self.sleepCount()
        elif(self.today == 6):
            self.saturday = self.sleepCount()
        elif(self.today == 7):
            self.sunday = self.sleepCount()
    
    def reset(self): #call once a week
        self.monday = 0
        self.tuesday = 0
        self.wednesday = 0
        self.thursday = 0
        self.friday = 0
        self.saturday = 0
        #do not reset sunday
        self.weekSum = 0
        self.timeSlept = 0
        self.sleepDate = 0
        self.wakeUpDate = 0
        self.timeStopSleep = 0
        #do not reset today

# users = [User(i["username"], i["sleepData"]["timeSlept"], i["sleepData"]["timeStopSleep"], i["sleepData"]["weekSum"], i["sleepData"]["sleepDate"], i["sleepData"]["wakeUpDate"], i["sleepData"]["monday"], i["sleepData"]["tuesday"], i["sleepData"]["wednesday"], i["sleepData"]["thursday"], i["sleepData"]["friday"], i["sleepData"]["saturday"], i["sleepData"]["sunday"], i["sleepData"]["today"]) for i in data]

def processUser(timeSlept, timeStopSleep, weekday, username, raw):
    with open('users.json') as a:
        data = json.load(a)
        print(data)
        for user in data:
            if user["username"] == username:
                if user["sleepData"] == "null":
                    processingUser = User(user["username"], timeSlept, timeStopSleep, weekday,  weekday, weekday+1, today=weekday)
                else:
                    processingUser = User(user["username"], timeSlept, timeStopSleep, weekday,  weekday, weekday+1, user["sleepData"]["monday"], user["sleepData"]["tuesday"], user["sleepData"]["wednesday"], user["sleepData"]["thursday"], user["sleepData"]["friday"], user["sleepData"]["saturday"], user["sleepData"]["sunday"], weekday)
                processingUser.todaySleep()
                processingUser.amountSleptCompare()
                finalData = {}
                finalData["timeSlept"] = processingUser.timeSlept
                finalData["timeStopSleep"] = processingUser.timeStopSleep
                finalData["weekSum"] = processingUser.weekSum
                finalData["sleepDate"] = processingUser.sleepDate
                finalData["wakeUpDate"] = processingUser.wakeUpDate
                finalData["monday"] = processingUser.monday
                finalData["tuesday"] = processingUser.tuesday
                finalData["wednesday"] = processingUser.wednesday
                finalData["thursday"] = processingUser.thursday
                finalData["friday"] = processingUser.friday
                finalData["saturday"] = processingUser.saturday
                finalData["sunday"] = processingUser.sunday
                finalData["today"] = processingUser.today   
                if user["sleepData"] != "null" and "raw" in user["sleepData"]:
                    finalData["raw"] = user["sleepData"]["raw"]
                    finalData["raw"].append(raw)
                else:
                    finalData["raw"] = [raw]

                with open("users.json", "w") as userFile:
                    user["sleepData"] = finalData
                    userFile.write(json.dumps(data))
                


# def leaderboard():
#     return users.sort(key=lambda x: x.weekSum, reverse=True)

# with open('quotes.txt', 'r', encoding='utf-8') as f:
#     quotes = [line.strip() for line in f]

# def getMessage(): #just call this function once a day
#     return random.choice(quotes)
