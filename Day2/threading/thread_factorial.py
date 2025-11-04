"""
Factorial with threads
# adopted from
http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/
"""

import threading
import time
import random


class FactorialThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    @staticmethod
    def factorial(n):
        result= n * FactorialThread.factorial(n - 1)
        
        results.append(result)

    def run(self):
        result = self.factorial(self.number)
        time.sleep(random.randint(5, 20))
        print(f"{self.number}! = {result}")


threads = [FactorialThread(number) for number in range(10)] # create thread object
[t.start()for t in threads] # starts all threads
threads[0].join()

