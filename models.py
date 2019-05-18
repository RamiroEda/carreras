import time
from log import Log
import requests
#from main import Main


class Conductor:
    TAG = "Conductor"

    def __init__(self, c_id):
        self.id = c_id
        self.lapCount = 0
        self.totalTime = 0.0
        self.initTime = time.time()
        self.lapTime = self.initTime

    def can_update(self, unix_time):
        return unix_time - self.lapTime > 5

    def update_time(self, unix_time):
        if self.can_update(unix_time):
            self.totalTime += unix_time - self.lapTime
            self.initTime = self.lapTime
            self.lapTime = unix_time
            self.lapCount += 1
            Log.d(self.TAG,
                  str(self.id) + ' ==> Vuelta #' + str(self.lapCount) + '. Tiempo: ' + str(self.lapTime - self.initTime)
                  + '. Tiempo total: ' + str(self.totalTime))
            self.update_database(self)


    @staticmethod
    def time_to_duration(time):
        dias = 0
        horas = 0
        minutos = 0
        segundos = 0

        if(time >= 86400):
            dias = int(time/86400)
            time %= 86400

        if(time >= 3600):
            horas = int(time/3600)
            time %= 3600

        if(time >= 60):
            minutos = int(time/60)
            time %= 60

        segundos = time

        return str(dias)+" "+str(horas)+":"+str(minutos)+":"+str(segundos)

    @staticmethod
    def update_database(driver):
        params = {
            'equipo': driver.id,
            'tiempo_total': Conductor.time_to_duration(driver.totalTime),
            'tiempo_vuelta': Conductor.time_to_duration(driver.lapTime - driver.initTime),
            'vuelta': driver.lapCount
        }
        req = requests.post("http://192.168.137.1:80/listaVueltas/", params)

        print(req.text)
