## Thread Vs Process Pull
# For Square number print example

# Claim : Threading is generally faster than multiprocessing for I/O-bound tasks due to lower overhead.
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
Output:
Square of 1: 1
Square of 2: 4
Square of 3: 9
Square of 4: 16
Square of 5: 25
Square of 6: 36
Square of 7: 49
Square of 8: 64
Time taken: 3.1888701915740967 seconds
'''

'''
FINAL SUMMARY: ThreadPoolExecutor vs ProcessPoolExecutor

THREAD POOL
-----------
ThreadPoolExecutor is fast when the task is mostly waiting (like sleep, I/O).
Square calculation is very small and takes almost no CPU time.
When one thread is waiting, another thread can run immediately.
Thread creation is lightweight, so there is very little overhead.
That is why ThreadPoolExecutor is faster for this code.

PROCESS POOL
------------
ProcessPoolExecutor also runs tasks in parallel, but it creates new processes.
Each process has its own memory, so data must be transferred between processes.
Process creation and data transfer take extra time.
For small tasks like square + sleep, this extra time makes it slower.
But for heavy CPU calculations, ProcessPoolExecutor becomes faster.

'''