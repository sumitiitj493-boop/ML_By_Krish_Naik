## Thread Vs Process Pull
# For Square number print example
from concurrent.futures import ThreadPoolExecutor
import time

def compute_square(number):
    time.sleep(1)  # Simulating I/O operation.
    return f"Square of {number}: {number * number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
if __name__ == '__main__':
    start_time = time.time()
    # Using ThreadPoolExecutor to manage threads
    with ThreadPoolExecutor(max_workers=3) as executor:
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
Time taken: 3.0039613246917725 seconds
'''