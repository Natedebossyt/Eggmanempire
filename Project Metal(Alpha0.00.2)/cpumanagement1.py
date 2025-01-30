class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time

class CPUManager:
    def __init__(self):
        self.queue = []

    def add_process(self, process):
        self.queue.append(process)

    def run_scheduler(self, time_slice):
        while self.queue:
            current_process = self.queue.pop(0)
            if current_process.remaining_time > time_slice:
                print(f"Process {current_process.pid} is executing for {time_slice} time units.")
                current_process.remaining_time -= time_slice
                self.queue.append(current_process)
            else:
                print(f"Process {current_process.pid} is executing for {current_process.remaining_time} time units.")
                current_process.remaining_time = 0
                print(f"Process {current_process.pid} completed execution.")
    
    def display_queue(self):
        print("Current Queue:")
        for process in self.queue:
            print(f"PID: {process.pid}, Burst Time: {process.burst_time}, Remaining Time: {process.remaining_time}")

# Example usage:
cpu_manager = CPUManager()

# Add processes to the queue
cpu_manager.add_process(Process(1, 10))
cpu_manager.add_process(Process(2, 5))
cpu_manager.add_process(Process(3, 8))

# Display the initial queue
cpu_manager.display_queue()

# Run the scheduler with a time slice of 4 units
cpu_manager.run_scheduler(4)

# Display the updated queue after running the scheduler
cpu_manager.display_queue()

import storagemanagement