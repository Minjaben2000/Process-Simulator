import Process
import queue
import RoundRobin
from collections import deque

class MultiFeedbackQueue(Process.Process):
    def __init__(self, ID, BurstTime, Priority, Arrival):
        super().__init__(ID, BurstTime, Priority, Arrival)
        self.remainingBurstTime = self.BurstTime

def run(process_set):
    process_queue = []
    for process in process_set:
        fqprocess = MultiFeedbackQueue(process.ID, process.BurstTime, process.Priority, process.Arrival)
        process_queue.append(fqprocess)

    sets = __sort__(process_queue)

    print("Running High Priority Queue\n")
    __runRobinThread__(sets[0], 2,12)
    print("Running Mid Priority Queue\n")
    __runRobinThread__(sets[1], 4, 12)
    #print("Running Low Priority Queue\n")
    #__runLowQueue__(sets[2], 12)
    process_queue = sets[0] + sets[1] + sets[2]
    sets = __sort__(process_queue)

#--------------------------------------------------------------------------------------------------------------------
#Sorts a set of processes into 3 queues based on priority
#process_set
#--------------------------------------------------------------------------------------------------------------------
def __sort__(process_set):
    process_set.sort(key=lambda x: x.Priority)
    LowerParse = int((len(process_set)/3)) #pointer splitting lower priority processes off
    UpperParse = int((len(process_set) * 2)/3) #pointer splitting higher priority processes off
    sets = []
    sets.append(process_set[UpperParse:(len(process_set))])
    sets.append(process_set[LowerParse:UpperParse])
    sets.append(process_set[0:LowerParse])
    sets[0].sort(key=lambda x: x.Arrival)
    sets[1].sort(key=lambda x: x.Arrival)
    sets[2].sort(key=lambda x: x.Arrival)


    print("High queue\n", sets[0])
    print("Mid queue\n", sets[1])
    print("Low queue\n", sets[2])

    return sets

#--------------------------------------------------------------------------------------------------------------------
#Round Robin scheduling algorithm
#process_set - set of processes to be scheduled
#quantum - time quantum for round robin
#runtime - amount of time at most that the algorithm will run for until next priority update
#--------------------------------------------------------------------------------------------------------------------
def __runRobinThread__(process_set, quantum : int, runtime : int):
    ready_queue = deque() # Used a deque to manage the ready processes in a round-robin fashion
    processesRan = [] #Tracking which processes have been run, to update priorities of processes that have not ran
    threads = []
    initlen = len(process_set) #initial length of process_set

    for process in process_set:
        RRprocess = RoundRobin.RRobin(process.ID, process.BurstTime, process.Priority, process.Arrival, 2)
        threads.append(RRprocess)
        RRprocess.start()

    trackedTime = 0
    currentTime = 0

    for t in threads:
        ready_queue.append(t)

    while ready_queue and trackedTime < runtime:
        process = ready_queue.popleft()
        temp = process_set.pop(0)
        processesRan.append(temp) #add process to processes ran

        print(f"\nTime {currentTime}s: Scheduler gives CPU to p{process.ID}")

        process.pause_event.clear()
        process.run_event.set()

        process.pause_event.wait()

        exeTime = min(quantum, process.remainingBurstTime, (runtime - trackedTime))
        currentTime += exeTime
        trackedTime += exeTime

        # Testing line to see what current time is being set to
        # print(f"Current time: {currentTime}s")
        process.remainingBurstTime -= exeTime
        temp.lowerBurstTime(exeTime)

        if process.remainingBurstTime > 0:
            print(f"p{process.ID} preempted, re-queued")
            ready_queue.append(process)
            process_set.append(temp)
        else:
            print(f"p{process.ID} finished at {currentTime}s")
            process.finished = True
            process.run_event.set()
            process.join()

    if len(processesRan) >= initlen:
        print("All processes ran")
        for i in range(len(process_set)):
            if (process_set[i].Priority > 0):
                process_set[i].setPriority(process_set[i].Priority - 1)
    else:
        print("Some processes ran")
        for i in range(len(process_set)):
            if (i < len(processesRan)-1):
                process_set[i].setPriority(process_set[i].Priority + 1) #processes that have not run
            else:
                process_set[i].setPriority(process_set[i].Priority - 1) #processes that have run
    print(process_set)




def __runLowQueue__(process_set, runtime : int):
    """This function accepts an iterable of Process objects
    :param process_set: iterable of Process objects
    :return: List of FirstComeProcess objects
    """
    run_list = []
    trackedTime = 0
    while not (len(process_set) == 0) and trackedTime < runtime:
        process = process_set.pop(0)
        process.start()
        print(f"Process {process.ID} started")
        process.join()
        run_list.append(process)
        print(f"Process {process.ID} finished")

    return run_list

if __name__ == "__main__":
    p1 = Process.Process(1, 4, 1, 3)
    p2 = Process.Process(2, 4, 2, 0)
    p3 = Process.Process(3, 4, 3, 1)
    p4 = Process.Process(4, 10, 1, 3)
    p5 = Process.Process(5, 10, 2, 0)
    p6 = Process.Process(6, 10, 0, 1)
    p7 = Process.Process(7, 10, 3, 2)
    toRun = [p1, p2, p3, p4, p5, p6, p7]

    print(run(toRun))