from math import sqrt
from itertools import islice
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
class PrimeGenerator():
    def __init__(self):
        self._cur = 2
    def __iter__(self):
        return self
    def __next__(self):
        while not is_prime(self._cur):
            self._cur += 1
        val = self._cur
        self._cur += 1
        return val
def prime(number):
    if number == 0:
        raise ValueError('non è primo')
    return next(islice(PrimeGenerator(), number - 1, number))