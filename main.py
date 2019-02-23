from list import ListConductor
from models import Conductor
from reader import Reader
from log import Log
import requests

TAG = "MAIN"

class Main:
    def __init__ (self):
        self.drivers = ListConductor()
        self.reader = Reader(self)
        self.waitForReader()

    def checkQueue(self):
        if(self.reader.queue.isEmpty()):
            return False
        else:
            return True

    def waitForReader(self):
        Log.i(TAG, "Esperando lector...")
        while(self.reader.isRunning == False): #Espera hasta que el lector serial se inicie
            pass
        self.initLoop()

    def initLoop(self):
        Log.i(TAG, "Proceso principal iniciado")
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
                    Log.i(TAG, str(queueElement[0])+' registrado.')
            elif(self.reader.isRunning == False):
                break
        Log.i(TAG, "Proceso principal terminado")
        self.waitForReader()

    def updateDatabase(self, driver):
        params = {
            'zzz':'yyy'
        }
        req = requests.post("www", params)

        print(req.text)
    
Main()