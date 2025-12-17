# Thread Vs Process Pull
# For Heavy CPU-bound example
from concurrent.futures import ThreadPoolExecutor
import time

def heavy_task(n):
    total = 0
    for i in range(10_000_000):   # heavy CPU work
        total += i * i
    return total

if __name__ == '__main__':
    start = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(heavy_task, [1, 2, 3, 4]))

    end = time.time()
    print("ThreadPool Time:", end - start)

# Output : ThreadPool Time: 2.2788469791412354