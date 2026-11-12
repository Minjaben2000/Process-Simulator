from Process import *
from collections import deque
import time

class RRobin(Process):
    #Constructor-------------------------------------------------------------------
    def __init__(self, ID, BurstTime, Priority, Arrival, timeQuantum):
        super().__init__(ID, BurstTime, Priority, Arrival)
        self.timeQuantum = timeQuantum

        self.remainingBurstTime = self.BurstTime
        
        self.finished = False

    # Override the run method for round-robin
    def run(self):
        print(f"[Thread] p{self.ID} initialized")

        while self.remainingBurstTime > 0 and not self.finished:
            self.run_event.wait()
            self.run_event.clear()
            
            if self.finished:
                break
            
            exeTime = min(timeQuantum, self.remainingBurstTime)
            print(f"p{self.ID} running for {exeTime} time units (Remaining: {self.remainingBurstTime - exeTime}s)")

            time.sleep(exeTime)

            self.pause_event.set()

#-------------------------------------------------------------------
def runThread(process_set, quantum):
    ready_queue = deque() # Used a deque to manage the ready processes in a round-robin fashion
    threads = []

    for process in process_set:
        RRprocess = RRobin(process.ID, process.BurstTime, process.Priority, process.Arrival)
        threads.append(RRprocess)
        RRprocess.start()

    currentTime = 0

    for t in threads:
        ready_queue.append(t)

    while ready_queue:
        process = ready_queue.popleft()

        print(f"\nTime {currentTime}s: Scheduler gives CPU to p{process.ID}")

        process.pause_event.clear()
        process.run_event.set()

        process.pause_event.wait()

        exeTime = min(quantum, process.remainingBurstTime)
        currentTime += exeTime
        # Testing line to see what current time is being set to
        # print(f"Current time: {currentTime}s")
        process.remainingBurstTime -= exeTime

        if process.remainingBurstTime > 0:
            print(f"p{process.ID} preempted, re-queued")
            ready_queue.append(process)
        else:
            print(f"p{process.ID} finished at {currentTime}s")
            process.finished = True
            process.run_event.set()
            process.join()



if __name__ == "__main__":
    p1 = Process(1, 9, 0, 0)
    p2 = Process(2, 5, 0, 1)
    p3 = Process(3, 3, 0, 2)
    p4 = Process(4, 13, 0, 3)
    processSet = [p1, p2, p3, p4]
    runThread(processSet, 2)
