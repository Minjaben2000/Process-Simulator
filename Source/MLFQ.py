import Process
import queue
import RoundRobin

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
    RoundRobin.runThread(sets[0], 2)
    print("Running Mid Priority Queue\n")
    RoundRobin.runThread(sets[1], 4)
    print("Running Low Priority Queue\n")
    __runLowQueue__(sets[2])


#Sorts a set of processes into 3 queues based on priority ----------------------------------------------------------
def __sort__(process_set):
    process_set.sort(key=lambda x: x.Priority)
    LowerParse = process_set[int((len(process_set)/3) - 1)].Priority
    UpperParse = process_set[int((len(process_set) * 2)/3)].Priority
    LowQueue = process_set[0:LowerParse]
    MidQueue = process_set[LowerParse:UpperParse]
    HighQueue = process_set[UpperParse:(len(process_set)-1)]
    sets = []
    sets.append(HighQueue)
    sets.append(MidQueue)
    sets.append(LowQueue)
    return sets

def __runLowQueue__(process_set):
    """This function accepts an iterable of Process objects
    :param process_set: iterable of Process objects
    :return: List of FirstComeProcess objects
    """
    run_list = []
    while not (len(process_set) == 0):
        process = process_set.pop()
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
    toRun = [p1, p2, p3]

    print(run(toRun))