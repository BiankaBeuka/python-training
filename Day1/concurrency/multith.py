"""
Factorial with threads
# adopted from
http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/
"""

import threading
import time
import random

# the Global Interpreter Lock (GIL) in CPython means that only one thread can execute Python bytecode at a time.
# Python is capable of executing only one instruction at a time 
class FactorialThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    @staticmethod
    def factorial(n):
        return (
            1 if n == 0
            else n * FactorialThread.factorial(n - 1)
        )

    def run(self):
        result = self.factorial(self.number)
        time.sleep(random.randint(5, 20))
        print(f"{self.number}! = {result}")


for number in range(10):
    FactorialThread(number).start()