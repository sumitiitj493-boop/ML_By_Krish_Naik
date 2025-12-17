# Use cases : Factorial of large numbers is CPU intensive task.we can use multiprocessing to speed it up by distributing the workload across multiple CPU cores.

import multiprocessing
import math
import sys  # For setting recursion limit
import time

# Allow large number operations
sys.setrecursionlimit(10**6)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    return f"Factorial of {number} computed."

if __name__ == '__main__':
    numbers = [50000, 60000, 70000, 80000]  # Large numbers for factorial computation
    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool(4) as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)

        for res in results:
            print(res)

    end_time = time.time()
    print(f"Time taken for factorial computations: {end_time - start_time} seconds")



    '''
    ╔══════════════════════════════════════════════════════════╗
║                    PROGRAM START                         ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║                    IMPORT MODULES                        ║
╠══════════════════════════════════════════════════════════╣
║  multiprocessing → create multiple processes             ║
║  math            → factorial computation                 ║
║  sys             → recursion limit control               ║
║  time            → execution time measurement            ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║              SET SYSTEM CONFIGURATION                    ║
╠══════════════════════════════════════════════════════════╣
║  sys.setrecursionlimit(10^6)                              ║
║  (Safety for very large computations)                    ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║              DEFINE WORKER FUNCTION                      ║
╠══════════════════════════════════════════════════════════╣
║  compute_factorial(number):                              ║
║   • Print status message                                 ║
║   • math.factorial(number) → CPU-bound work              ║
║   • Return completion message                            ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║           MAIN PROCESS ENTRY CHECK                       ║
╠══════════════════════════════════════════════════════════╣
║  if __name__ == "__main__":                               ║
║  (Required for multiprocessing on Windows)               ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║                 INPUT DATA SET                           ║
╠══════════════════════════════════════════════════════════╣
║  numbers = [50000, 60000, 70000, 80000]                  ║
║  (4 independent CPU-intensive tasks)                     ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║               START TIME RECORD                          ║
╠══════════════════════════════════════════════════════════╣
║  start_time = time.time()                                ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║            CREATE MULTIPROCESSING POOL                   ║
╠══════════════════════════════════════════════════════════╣
║  Pool(processes = 4)                                     ║
║  • 4 child processes created by OS                       ║
║  • Each process → separate memory & CPU core             ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║             PARALLEL TASK DISTRIBUTION                   ║
╠══════════════════════════════════════════════════════════╣
║  pool.map(compute_factorial, numbers)                    ║
║                                                          ║
║   ┌────────────┐   ┌────────────┐                        ║
║   │ Process 1  │→→ │ fact(50000)│                        ║
║   └────────────┘   └────────────┘                        ║
║   ┌────────────┐   ┌────────────┐                        ║
║   │ Process 2  │→→ │ fact(60000)│                        ║
║   └────────────┘   └────────────┘                        ║
║   ┌────────────┐   ┌────────────┐                        ║
║   │ Process 3  │→→ │ fact(70000)│                        ║
║   └────────────┘   └────────────┘                        ║
║   ┌────────────┐   ┌────────────┐                        ║
║   │ Process 4  │→→ │ fact(80000)│                        ║
║   └────────────┘   └────────────┘                        ║
║                                                          ║
║  (True parallel execution on multiple CPU cores)         ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║             SYNCHRONIZATION POINT                        ║
╠══════════════════════════════════════════════════════════╣
║  pool.map waits until ALL processes finish               ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║                COLLECT RESULTS                           ║
╠══════════════════════════════════════════════════════════╣
║  results = [messages returned by each process]           ║
║  (Order same as input list)                              ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║                 DISPLAY OUTPUT                           ║
╠══════════════════════════════════════════════════════════╣
║  Print status of each factorial computation              ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║             CLEANUP & RESOURCE RELEASE                   ║
╠══════════════════════════════════════════════════════════╣
║  Pool auto-closes                                        ║
║  Child processes terminated                              ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║               END TIME RECORD                            ║
╠══════════════════════════════════════════════════════════╣
║  end_time = time.time()                                  ║
║  total_time = end_time - start_time                      ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║                FINAL OUTPUT                              ║
╠══════════════════════════════════════════════════════════╣
║  Print total execution time                              ║
╚══════════════════════════════════════════════════════════╝
                            │
                            ▼
╔══════════════════════════════════════════════════════════╗
║                    PROGRAM END                           ║
╚══════════════════════════════════════════════════════════╝

    '''
