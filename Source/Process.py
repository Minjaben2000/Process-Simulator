import threading
import time

class Process(object):
    __ID = 0
    __BurstTime = 0
    __Priority = 0
    __Arrival = 0

    def __init__(self, ID, BurstTime, Priority, Arrival):
        self.__ID = ID
        self.__BurstTime = BurstTime
        self.__Priority = Priority
        self.__Arrival = Arrival
    
    def __work():
        # do work
        time.sleep(1)

    __task = threading.Thread(target=__work);

    def start():
        __task.start()

    def join():
        __task.join()