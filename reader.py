import threading
import serial
import time
from list import List

class Reader:
    def __init__(self):
        self.queue = List()
        self.isRunning = False
        threading.Thread(target=self.initReader).start()

    def initReader(self):
        self.serialPort = serial.Serial('COM6', 9600) #TODO: Cambiar el puerto si lo necesitamos
        self.isRunning = True
        while True:
            try:
                self.queue.push_back([self.serialPort.readline(), time.time()])
            except:
                print('Error en la lectura del puerto serial')
                break

        self.isRunning = False
        self.serialPort.close()