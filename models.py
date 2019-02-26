import time
from log import Log


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
