import json

with open('data.json') as file:
    data = json.load(file)

class user:
    def __init__(self,
                user:str,
                timeSlept:int,
                timeStopSleep:int,
                weekSum:int,
                sleepDate:int,
                wakeUpDate:int,
                monday:int,
                tuesday:int,
                wednesday:int,
                thursday:int,
                friday:int,
                saturday:int,
                sunday:int,
                today:int):
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
    
    def todaySleep(self):
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

users = [user(i["user"], i["timeSlept"], i["timeStopSleep"], i["weekSum"], i["sleepDate"], i["wakeUpDate"], i["monday"], i["tuesday"], i["wednesday"], i["thursday"], i["friday"], i["saturday"], i["sunday"], i["today"]) for i in data]
    