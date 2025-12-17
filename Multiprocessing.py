import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1) # Simulating I/O operation.
        print(f"Square : {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5) # Simulating I/O operation.
        print(f"Cube : {i * i * i}")
if __name__ == '__main__':    # The below code will only run if this script is executed directly.If imported, it won't run.
                              # __main__ Python ka inbuilt (reserved) name hai, jo tab set hota hai jab file direct run hoti hai.
                              # file_name koi inbuilt nahi hota, wo file ka actual naam hota hai jab file import hoti hai.
    # Create processes for each function
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)
    # Start the timer
    start_time = time.time()
    # Start the processes
    process1.start()
    process2.start()
    # Wait for both processes to complete
    process1.join()
    process2.join()
    # Stop the timer
    end_time = time.time()
    print(f"Total time with multiprocessing : {end_time - start_time} seconds")