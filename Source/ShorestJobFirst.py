import time
from Process import Process

class ShortestJobFirst:
  def __init__(self, processes):
    self.processes = processes

  def schedule(self):
    ready_queue = []
    completed = []
    current_time = 0

  # Sort Processes by arrival time initally
  processes = sorted(self.processes, key=lambda p: o.Arrival)

  while processes or ready_queue:
    # Add processes that have arrived to the ready queue
    while processes and processes[0].Arrival <= current_time:
      ready_queue.append(processes.pop(0))

  # If no process is ready, wait for the next arrival
  if not ready_queue:
    next_process = processes[0]
    wait_time = next_process.Arrival - current_time

    print(f"CPU idle for {wait_time} seconds\n")
    time.sleep(wait_time)
    current_time = next_process.Arrival
    continue

  # Select the process with the shortest burst time
  shortest_process = min(ready_queue, key=lambda p: p.BurstTime)

  ready_queue.remove(shortest_process)

  print(f"Scheduling: {shortest_process}")

  # Runt the selected process
  current_time += shortest_process.BurstTime

  completed.append(shortest_process)

  # Add processes that arrived while the CPU was busy
  while processes and processes[0].Arrival <= current_time:
    ready_queue.append(processes.pop(0))

print("\nAll processes have completed.")

return completed

if __name__ == "__main__":
  p1 = Process(1, 8, 2, 0)
  p2 = Process(2, 4, 1, 1)
  p3 = Process(3, 1, 3, 2)
  p4 = Process(4, 5, 2, 3)

  processes = [p1, p2, p3, p4]

  # Create the SJF scheduler
  sjf = ShortestJobFirst(processes)

  # Schedule the Process
  sjf.schedule()
  

