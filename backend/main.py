import json
import random

with open('data.json') as a:
    data = json.load(a)

class User:
    def __init__(self,
                user:str=None,
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
        self.user = user
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

users = [User(i["user"], i["timeSlept"], i["timeStopSleep"], i["weekSum"], i["sleepDate"], i["wakeUpDate"], i["monday"], i["tuesday"], i["wednesday"], i["thursday"], i["friday"], i["saturday"], i["sunday"], i["today"]) for i in data]

def leaderboard():
    return users.sort(key=lambda x: x.weekSum, reverse=True)

with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f]

def getMessage(): #just call this function once a day
    return random.choice(quotes)
