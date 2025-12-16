# Project Structure:
#                Arithmetic_project
#                       /   \
#                      /     \
#                   app.py   app.log
#                            (Auto-created when the app runs)
import logging
# Configure logging with handelers
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
        logging.FileHandler('app.log'),  # Log to file
        logging.StreamHandler()  # Log to console

    ]
)
# Create logger for this module
logger=logging.getLogger("arithmetic_app")
# Addition 
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}") 
    return result
# Subtraction function
def subtract(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}") 
    return result
# Subtraction function
def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result
# Multiplication function
def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result
# Division function with error handling
def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Error: Division by zero!")
        return None
# Example usage
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
divide(10, 0) #This will log an error
logger.info("Arithmetic operations completed.")


