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
   
from multiprocessing import Process, Lock, Pool
from multiprocessing import Queue

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-i*i)

if __name__ == '__main__':
    q = Queue()
    numbers = range(10)
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())