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

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for i in range(len(numbers)):
                numbers[i] += 1

if __name__ == '__main__':
   lock = Lock()
   shared_array = Array('d', [0.0, 100.0, 200.0])
   print('Array at beginning is: ', shared_array[:])

   p1 = Process(target=add_100, args=(shared_array, lock))
   p2 = Process(target=add_100, args=(shared_array, lock))

   p1.start()
   p2.start()

   p1.join()
   p2.join()

   print('Array at beginning is: ', shared_array[:])


    