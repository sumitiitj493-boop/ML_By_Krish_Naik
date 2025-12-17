from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)  # Simulating I/O operation.
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Using ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=3) as executor:   
    start_time = time.time()

    # Map function to the list of numbers
    results = executor.map(print_number, numbers) # map ka kaam = values ko function me bhejna
                                                      # queue ka kaam = extra tasks ko line me wait karwana

    for result in results:
        print(result)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

# Note: The ThreadPoolExecutor automatically manages the creation and destruction of threads.
# The max_workers parameter defines the maximum number of threads that can be used to execute the given
'''

Numbers list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        |
        v
     Queue (waiting line)
        |
        v
3 Threads take work one by one
        |
        v
Function runs
        |
        v
Result returned



ThreadPoolExecutor Flow Diagram

Main Thread
   |
   |-- Create ThreadPoolExecutor (max_workers = 3)
   |
   |-- executor.map(print_number, numbers)
   |        |
   |        |-- Thread 1 --> print_number(1) --> sleep --> return "Number: 1"
   |        |-- Thread 2 --> print_number(2) --> sleep --> return "Number: 2"
   |        |-- Thread 3 --> print_number(3) --> sleep --> return "Number: 3"
   |        |
   |        |-- Thread 1 --> print_number(4)
   |        |-- Thread 2 --> print_number(5)
   |        |-- Thread 3 --> print_number(6)
   |        |
   |        |-- Thread 1 --> print_number(7)
   |        |-- Thread 2 --> print_number(8)
   |        |-- Thread 3 --> print_number(9)
   |        |
   |        |-- Thread 1 --> print_number(10)
   |
   |-- Results returned in ORDER (1 to 10)
   |
   |-- for loop prints results one by one
   |
   |-- END

'''