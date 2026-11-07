import Process
import queue

# This function accepts a set
def run(process_set):
    process_queue = queue.Queue()
    for process in process_set:
        process_queue.put(process)

    while not process_queue.empty():
        process = process_queue.get()
        process.start()
        print(f"Process {process.ID} started")
        process.join()
        print(f"Process {process.ID} finished")

if __name__ == '__main__':
    p1 = Process.Process(1, 1, 0, 0)
    p2 = Process.Process(2, 1, 0, 0)
    p3 = Process.Process(3, 1, 0, 0)
    toRun = [p1, p2, p3]

    run(toRun)