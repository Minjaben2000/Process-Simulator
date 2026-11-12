import threading
import time





class Process(threading.Thread):
    __ID = 0
    __BurstTime = 0
    __Priority = 0
    __Arrival = 0

    def __init__(self, ID: int, BurstTime: int, Priority: int, Arrival: int):
        super().__init__()
        self.__ID = ID
        self.__BurstTime = BurstTime
        self.__Priority = Priority
        self.__Arrival = Arrival

        # Events used to coordinate processes within the scheduler
        self.run_event = threading.Event()
        self.pause_event = threading.Event()

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
        if not isinstance(other, Process):
            return False
        return self.__ID == other.ID

    def __hash__(self) -> int:
        return hash(self.__ID)

    def __str__(self) -> str:
        return f"Id: {self.__ID} BurstTime: {self.__BurstTime} Priority: {self.__Priority} Arrival: {self.__Arrival}"

    def __repr__(self) -> str:
        return f"<Process ID={self.__ID}, BurstTime={self.__BurstTime}, Priority={self.__Priority}, Arrival={self.__Arrival}>"

    def run(self):
        print(f"p{self.__ID} running\n")
        time.sleep(self.__BurstTime)
        print(f"p{self.__ID} stopping\n")

