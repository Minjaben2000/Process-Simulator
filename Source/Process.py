import threading
import time

class Process(object):
    __ID = 0
    __BurstTime = 0
    __Priority = 0
    __Arrival = 0

    def __init__(self, ID: int, BurstTime: int, Priority: int, Arrival: int):
        self.__ID = ID
        self.__BurstTime = BurstTime
        self.__Priority = Priority
        self.__Arrival = Arrival

    @property
    def ID(self):
        return self.__ID

    @property
    def BurstTime(self):
        return self.__BurstTime

    @property
    def Priority(self):
        return self.__Priority

    @property
    def Arrival(self):
        return self.__Arrival

    def __eq__(self, other) -> bool:
        return self.__ID == other.ID

    def __work(self):
        # do work
        time.sleep(1)

    __task = threading.Thread(target=__work)

    def start(self):
        self.__task.start()

    def join(self):
        self.__task.join()