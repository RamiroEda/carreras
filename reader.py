import threading
import serial
import time
from list import List
from log import Log

PORT = "COM6"  # TODO: Cambiar el puerto si lo necesitamos
TAG = "Lector"


class Reader:
    def __init__(self, main_thread):
        self.serial_port = None
        self.is_running = False
        self.queue = List()
        self.mainThread = main_thread

        self.wait_for_conection()

    def init_reader(self):
        self.serial_port = serial.Serial(PORT, 9600)
        self.is_running = True

        Log.i(TAG, "Lector iniciado")

        while True:
            if self.mainThread is None:
                Log.e(TAG, "El proceso principal no existe")
                del self
            try:
                self.queue.push_back([self.serial_port.readline(), time.time()])
            except:
                Log.e(TAG, "Error en la lectura del puerto " + PORT)
                break

        Log.i(TAG, "Lector apagado")

        self.serial_port.close()
        self.wait_for_conection()

    def wait_for_conection(self):
        self.is_running = False

        Log.i(TAG, "Esperando conexión en el puerto " + PORT + "...")

        while True:
            try:
                serial.Serial(PORT, 9600)
                break
            except:
                pass

        Log.i(TAG, "Conectado al puerto " + PORT)

        threading.Thread(target=self.init_reader).start()
