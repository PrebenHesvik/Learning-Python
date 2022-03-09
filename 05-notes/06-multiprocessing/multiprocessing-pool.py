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

def cube(number):
    return number * number * number

if __name__ == '__main__':
   numbers = range(10)
   pool = Pool()
   result = pool.map(cube, numbers)
   print(result)
   


    