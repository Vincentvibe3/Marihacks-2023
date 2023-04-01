import json
import random

with open('D:/SunWeiwei/Repo/Marihacks-2023/backend/users.json') as a:
    data = json.load(a)
    
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
        self.SleepData = [username, timeSlept, timeStopSleep, weekSum, sleepDate, wakeUpDate, monday, tuesday, wednesday, thursday, friday, saturday, sunday, today]

    def sleepCount(self):
        return self.SleepData[2] - self.SleepData[1] if self.SleepData[5] == self.SleepData[4] else 24 - self.SleepData[1] + self.SleepData[2]
    
    def amountSleptCompare(self): 
        if(self.SleepData[13] == 1):
            return self.SleepData[6] - self.SleepData[12]
        elif(self.SleepData[13] == 2):
            return self.SleepData[7] - self.SleepData[6]
        elif(self.SleepData[13] == 3):
            return self.SleepData[8] - self.SleepData[7]
        elif(self.SleepData[13] == 4):
            return self.SleepData[9]- self.SleepData[8]
        elif(self.SleepData[13] == 5):
            return self.SleepData[10] - self.SleepData[9]
        elif(self.SleepData[13] == 6):
            return self.SleepData[11] - self.SleepData[10]
        elif(self.SleepData[13] == 7):
            return self.SleepData[12] - self.SleepData[11]
    
    def todaySleep(self): #call once a day
        self.SleepData[3] += self.sleepCount()
        if(self.SleepData[13] == 1):
            self.SleepData[6] = self.sleepCount()
        elif(self.SleepData[13] == 2):
            self.SleepData[7] = self.sleepCount()
        elif(self.SleepData[13] == 3):
            self.SleepData[8] = self.sleepCount()
        elif(self.SleepData[13] == 4):
            self.SleepData[9] = self.sleepCount()
        elif(self.SleepData[13] == 5):
            self.SleepData[10] = self.sleepCount()
        elif(self.SleepData[13] == 6):
            self.SleepData[11] = self.sleepCount()
        elif(self.SleepData[13] == 7):
            self.SleepData[12] = self.sleepCount()
    
    def reset(self): #call once a week
        self.SleepData[6] = 0
        self.SleepData[7] = 0
        self.SleepData[8] = 0
        self.SleepData[9] = 0
        self.SleepData[10] = 0
        self.SleepData[11] = 0
        #do not reset sunday
        self.SleepData[3] = 0
        self.SleepData[1] = 0
        self.SleepData[4] = 0
        self.SleepData[5] = 0
        self.SleepData[2] = 0
        #do not reset today

    def __str__(self):
        return str(self.SleepData)

users = [User(i["username"], i["sleepData"]["timeSlept"], i["sleepData"]["timeStopSleep"], i["sleepData"]["weekSum"], i["sleepData"]["sleepDate"], i["sleepData"]["wakeUpDate"], i["sleepData"]["monday"], i["sleepData"]["tuesday"], i["sleepData"]["wednesday"], i["sleepData"]["thursday"], i["sleepData"]["friday"], i["sleepData"]["saturday"], i["sleepData"]["sunday"], i["sleepData"]["today"]) for i in data]

def leaderboard():
    return users.sort(key=lambda x: x.weekSum, reverse=True)

#with open('D:/SunWeiwei/Respo/Marihacks-2023/backend/quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f]

#def getMessage(): #just call this function once a day
    return random.choice(quotes)

print(users[1])
