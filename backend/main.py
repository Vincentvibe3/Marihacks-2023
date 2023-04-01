import time
import json
#import flask

def sleepCount(start:int, end:int):
    return end - start


#[{user:String, timeSlept:Int, timeStopSleep:Int, dayOfTheWeek:Int, weekSum:Int, sleepDate:Int, wakeupDate:Int, monday:Int, tuesday, wednesday, ...}, ...]
with open('data.json') as file:
    data = json.load(file)

#for i in data:
#    i["weekSum"] += sleepCount(i["timeSlept"], i["timeStopSleep"]) # 7 times

class user:
    def __init__(self,
                user,
                timeSlept,
                timeStopSleep,
                dayOfTheWeek,
                weekSum,
                sleepDate,
                wakeupDate,
                monday,
                tuesday,
                wednesday,
                thursday,
                friday,
                saturday,
                sunday,
                today):
        self.user = user
        self.timeSlept = timeSlept
        self.timeStopSleep = timeStopSleep
        self.dayOfTheWeek = dayOfTheWeek
        self.weekSum = weekSum
        self.sleepDate = sleepDate
        self.wakeupDate = wakeupDate
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.today = today
        #sleepCount = lambda self : self.timeStopSleep - self.timeSlept if self.wakeupDate == self.sleepDate else 24 - self.timeSlept + self.timeStopSleep

    def sleepCount(self):
        return self.timeStopSleep - self.timeSlept if self.wakeupDate == self.sleepDate else 24 - self.timeSlept + self.timeStopSleep
    
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
    
    def todaySleep(self):
        if(self.today == 1):
            self.monday = sleepCount()
        elif(self.today == 2):
            self.tuesday = sleepCount()
        elif(self.today == 3):
            self.wednesday = sleepCount()
        elif(self.today == 4):
            self.thursday = sleepCount()
        elif(self.today == 5):
            self.friday = sleepCount()
        elif(self.today == 6):
            self.saturday = sleepCount()
        elif(self.today == 7):
            self.sunday = sleepCount()


        
        
    users = [user(i["user"], i["timeSlept"], i["timeStopSleep"], i["dayofTheWeek"], i["weekSum"], i["sleepDate"], i["wakeuppDate"], i["monday"], i["tuesday"], i["wednesday"], i["thursday"], i["friday"], i["saturday"], i["sunday"], i["today"]) for i in data]
    