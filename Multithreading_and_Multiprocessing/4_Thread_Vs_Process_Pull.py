#Thread Vs Process Pull
# For Heavy CPU-bound example
from concurrent.futures import ProcessPoolExecutor
import time

def heavy_task(n):
    total = 0
    for i in range(10_000_000):   # heavy CPU work
        total += i * i
    return total

if __name__ == '__main__':
    start = time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(heavy_task, [1, 2, 3, 4]))

    end = time.time()
    print("ProcessPool Time:", end - start)


# Output:ProcessPool Time: 1.2240335941314697

'''
FINAL SUMMARY: ProcessPoolExecutor vs ThreadPoolExecutor
(CPU-Heavy Example)

THREAD POOL
-----------
ThreadPoolExecutor becomes slow when the task is CPU-heavy.
All threads run inside the same process and share the same CPU because of GIL.
Even if multiple threads exist, only one thread executes CPU code at a time.
So heavy loops do not run in true parallel.
That is why ThreadPoolExecutor is slow for heavy calculations.

PROCESS POOL
------------
ProcessPoolExecutor is fast for CPU-heavy tasks.
Each process runs independently on a separate CPU core.
There is no GIL restriction between processes.
Heavy calculations run truly in parallel.
That is why ProcessPoolExecutor is faster in this example.

'''