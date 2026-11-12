import Process
import queue


class FirstComeProcess(Process.Process):
    """Subclass of Process class to add ordering by arrival time"""
    def __init__(self, ID, BurstTime, Priority, Arrival):
        super().__init__(ID, BurstTime, Priority, Arrival)

    def __lt__(self, other):
        return self.Arrival < other.Arrival


# This function accepts an iterable of Process objects
def run(process_set) -> list[FirstComeProcess]:
    """This function accepts an iterable of Process objects
    :param process_set: iterable of Process objects
    :return: List of FirstComeProcess objects
    """
    process_queue = queue.PriorityQueue()
    for process in process_set:
        fcprocess = FirstComeProcess(process.ID, process.BurstTime, process.Priority, process.Arrival)
        process_queue.put(fcprocess)

    run_list = []
    while not process_queue.empty():
        process = process_queue.get()
        process.start()
        print(f"Process {process.ID} started")
        process.join()
        run_list.append(process)
        print(f"Process {process.ID} finished")

    return run_list


if __name__ == '__main__':
    p1 = Process.Process(1, 1, 0, 3)
    p2 = Process.Process(2, 1, 0, 0)
    p3 = Process.Process(3, 1, 0, 1)
    toRun = [p1, p2, p3]

    print(run(toRun))
