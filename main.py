from list import ListConductor
from models import Conductor
from reader import Reader
from log import Log
import requests

TAG = "MAIN  "


class Main:
    def __init__(self):
        self.drivers = ListConductor()
        self.reader = Reader(self)
        self.wait_for_reader()

    def check_queue(self):
        if self.reader.queue.is_empty():
            return False
        else:
            return True

    def wait_for_reader(self):
        Log.i(TAG, "Esperando lector...")
        while not self.reader.is_running:  # Espera hasta que el lector serial se inicie
            pass
        self.init_loop()

    def init_loop(self):
        Log.i(TAG, "Proceso principal iniciado")
        while True:
            if self.check_queue():
                queue_element = self.reader.queue.front()
                if self.drivers.contains(queue_element[0]):
                    driver = self.drivers.getDriverById(queue_element[0])
                    if driver != -1:
                        driver.update_time(queue_element[-1])

                    self.reader.queue.pop_front()
                else:
                    self.drivers.push_back(Conductor(queue_element[0]))
                    Log.i(TAG, str(queue_element[0]) + ' registrado.')
            elif not self.reader.is_running:
                break
        Log.i(TAG, "Proceso principal terminado")
        self.wait_for_reader()

    @staticmethod
    def update_database(driver):
        params = {
            'equipo': driver.id,
            'tiempo_total': driver.totalTime,
            'tiempo_vuelta': driver.lapTime,
            'vuelta': driver.lapTime
        }
        req = requests.post("http://127.0.0.1:8000/listaVueltas/", params)

        print(req.text)


Main()
