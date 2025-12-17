# Using ProcessPoolExecutor to manage processes


# What is ProcessPoolExecutor?
# ProcessPoolExecutor ek high-level interface hai jo multiple processes ko manage karta hai.


#How it is different from ThreadPoolExecutor?
# ThreadPoolExecutor threads ka use karta hai, jo same memory space share karte hain.
# ProcessPoolExecutor processes ka use karta hai, jo independent memory space share karte hain.
'''
THREAD POOL vs PROCESS POOL (Diagrammatic View)

THREAD POOL
===========

Single Process
+----------------------------------+
|          Main Process            |
|                                  |
|  Shared Memory                   |
|                                  |
|  +-----------+  +-----------+    |
|  | Thread 1  |  | Thread 2  |    |
|  | (Task A)  |  | (Task B)  |    |
|  +-----------+  +-----------+    |
|         +-----------+            |
|         | Thread 3  |            |
|         | (Task C)  |            |
|         +-----------+            |
|                                  |
|  All threads share same memory   |
|  Affected by GIL (CPU work)      |
+----------------------------------+



PROCESS POOL
============

Multiple Processes
+------------------+   +------------------+
|   Process 1      |   |   Process 2      |
|                  |   |                  |
|  +-----------+   |   |  +-----------+   |
|  | Task A    |   |   |  | Task B    |   |
|  +-----------+   |   |  +-----------+   |
|  Separate        |   |  Separate        |
|  Memory          |   |  Memory          |
+------------------+   +------------------+

        +------------------+
        |   Process 3      |
        |                  |
        |  +-----------+   |
        |  | Task C    |   |
        |  +-----------+   |
        |  Separate        |
        |  Memory          |
        +------------------+

Processes do NOT share memory
Not affected by GIL

'''
from concurrent.futures import ProcessPoolExecutor
import time

def compute_square(number):
    time.sleep(1)  # Simulating I/O operation.
    return f"Square of {number}: {number * number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
if __name__ == '__main__':
    start_time = time.time()
    # Using ProcessPoolExecutor to manage processes
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Map function to the list of numbers
        results = executor.map(compute_square, numbers)
        for result in results:
            print(result)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
'''

ThreadPoolExecutor vs ProcessPoolExecutor (Clear Comparison Table)

+----------------------+---------------------------+-----------------------------+
| Feature              | ThreadPoolExecutor        | ProcessPoolExecutor         |
+----------------------+---------------------------+-----------------------------+
| Execution Time       | Fast for I/O tasks        | Fast for CPU-heavy tasks    |
|                      | Slow for CPU tasks        | True parallel execution     |
+----------------------+---------------------------+-----------------------------+
| Execution Model      | Multiple threads          | Multiple processes          |
|                      | inside one process        | (separate processes)        |
+----------------------+---------------------------+-----------------------------+
| Memory               | Shared memory             | Separate memory             |
+----------------------+---------------------------+-----------------------------+
| GIL Effect           | Affected by GIL           | Not affected by GIL         |
+----------------------+---------------------------+-----------------------------+
| Startup Overhead     | Very low                  | High (process creation)     |
+----------------------+---------------------------+-----------------------------+
| Communication        | Easy (shared variables)   | Slower (pickle required)    |
+----------------------+---------------------------+-----------------------------+
| Crash Impact         | One thread crash can      | One process crash does not  |
|                      | affect whole process      | affect other processes      |
+----------------------+---------------------------+-----------------------------+
| Best For             | I/O-bound tasks           | CPU-bound tasks             |
|                      | (sleep, network, files)   | (math, image processing)    |
+----------------------+---------------------------+-----------------------------+
| Jupyter Notebook     | Works smoothly            | Often unreliable            |
+----------------------+---------------------------+-----------------------------+

'''
