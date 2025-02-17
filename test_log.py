import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start program: ')

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        logging.debug("Current %s: factorial is %s", i, factorial)
    return factorial


print(str(factorial(5)))

    
