import Process
import queue

class FirstComeProcess(Process.Process):
    def __init__(self, ID, BurstTime, Priority, Arrival):
        super().__init__(ID, BurstTime, Priority, Arrival)

    def __lt__(self, other):
        return self.Arrival < other.Arrival

# This function accepts a set
def run(process_set):
    process_queue = queue.PriorityQueue()
    for process in process_set:
        fcprocess = FirstComeProcess(process.ID, process.BurstTime, process.Priority, process.Arrival)
        process_queue.put(fcprocess)

    while not process_queue.empty():
        process = process_queue.get()
        process.start()
        print(f"Process {process.ID} started")
        process.join()
        print(f"Process {process.ID} finished")

if __name__ == '__main__':
    p1 = Process.Process(1, 1, 0, 3)
    p2 = Process.Process(2, 1, 0, 0)
    p3 = Process.Process(3, 1, 0, 1)
    toRun = [p1, p2, p3]

    run(toRun)