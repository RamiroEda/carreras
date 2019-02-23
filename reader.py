import threading
import serial
import time
from list import List
from log import Log

PORT = "COM6" #TODO: Cambiar el puerto si lo necesitamos
TAG = "Lector"

class Reader:
    def __init__(self, mainThread):
        self.queue = List()
        self.mainThread = mainThread

        self.waitForConection()

    def initReader(self):
        self.serialPort = serial.Serial(PORT, 9600)
        self.isRunning = True

        Log.i(TAG, "Lector iniciado")

        while True:
            if(self.mainThread is None):
                Log.e(TAG, "El proceso principal no existe")
                break
            try:
                self.queue.push_back([self.serialPort.readline(), time.time()])
            except:
                Log.e(TAG, "Error en la lectura del puerto "+PORT)
                break

        Log.i(TAG, "Lector apagado")

        self.isRunning = False
        self.serialPort.close()
        
        self.waitForConection()

    def waitForConection(self):
        self.isRunning = False

        Log.i(TAG, "Esperando conexión en el puerto "+PORT+"...")

        while True:
            try:
                serial.Serial(PORT, 9600)
                break
            except:
                pass

        Log.i(TAG, "Conectado al puerto "+PORT)
            
        threading.Thread(target=self.initReader).start()
