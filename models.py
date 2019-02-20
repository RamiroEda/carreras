import time

class Conductor:
    def __init__(self, id):
        self.id = id
        self.lapCount = 0
        self.totalTime = 0.0
        self.initTime = time.time()
        self.lapTime = self.initTime

    def canUpdate(self, time):
        return time-self.lapTime > 5

    def updateTimer(self, time):
        if(self.canUpdate(time)):
            self.totalTime += time-self.lapTime
            self.initTime = self.lapTime
            self.lapTime = time
            self.lapCount += 1
            print(str(self.id)+' ==> Vuelta #'+str(self.lapCount)+'. Tiempo: '+str(self.lapTime-self.initTime)+'. Tiempo total: '+str(self.totalTime))   

    def getId(self):
        return self.id