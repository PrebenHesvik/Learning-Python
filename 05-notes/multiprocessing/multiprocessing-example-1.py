#### Process: 
   # An instance of a program (e.g a Python interpreter)

#### Advantages:
   # - Takes advantage of multiple CPUs and cores
   # - Separate memory space --> memory is not shared between processes
   # - Great for CPU-bound processing
   # - Processes are interruptabøe/killable
   # - One GIL for each process --> avoids GIL limitation

#### Disadvantages:
   # - Heavyweight
   # - Starting a process is slower than starting a thread
   # - More memory
   # - IPC (inter-process communication) is more complicated
   
from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        
if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()

    # create processes:
    for _ in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()