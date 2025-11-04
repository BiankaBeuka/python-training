""" Use cases for decorators 
    - timing and logging of functions calls
    - many built-in decorators: @property, @staticmethod, @pytest.fixture, @fasapi.route, ...
    - undestand python on a deeper level
"""

from typing import Callable

class FailureCounter:

    def __init__(self, message):
        self.message = message
        self.function = None
        self.failcount = 0

    def __call__(self, func):
        self.function = func
        return self.safe_call

    def safe_call(self, *args):
        # extra functionaity that is added
        try:
            self.function(*args) # type: ignore # here we call risky)fileopen
        except Exception:
            self.failcount += 1
            print(self.message)
            print(f'An I/O error was caught in {self.function.__name__}')
            print(f"with the file name '{args[0]}'")
            print(f'this is failure #{self.failcount}\n')

@FailureCounter(message='--- zero ERROR ---')
def zero(a,b):
    return (a+b)/0

@FailureCounter('--- FILE ERROR ---')
def risky_fileopen(filename):
    open(filename)

risky_fileopen('not_existing_file') # looks as if we were calling risky_fileopen()
risky_fileopen('doesnotexist_either') # but we really call safe_call()

# risky_fileopen(filename='not_exis/ting_file')

zero(1,2)