from list import ListConductor
from models import Conductor
from reader import Reader

class Main:
    def __init__ (self):
        self.drivers = ListConductor()
        self.reader = Reader()
        while(self.reader.isRunning == False): #Espera hasta que el lector serial se inicie
            pass
        self.initLoop()
            

    def checkQueue(self):
        if(self.reader.queue.isEmpty()):
            return False
        else:
            return True

    def initLoop(self):
        while True:
            if(self.checkQueue()):
                queueElement = self.reader.queue.front()
                if(self.drivers.contains(queueElement[0])):
                    driver = self.drivers.getDriverById(queueElement[0])
                    if(driver != -1):
                        driver.updateTimer(queueElement[-1])

                    self.reader.queue.pop_front()
                else:
                    self.drivers.push_back(Conductor(queueElement[0]))
                    print(str(queueElement[0])+' registrado.')
            elif(self.reader.isRunning == False):
                break

    def updateDatabase(self, driver):
        pass
    
Main()