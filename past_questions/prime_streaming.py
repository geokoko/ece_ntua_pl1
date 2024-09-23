import math
class Primes:
    @staticmethod
    # Time Complexity: O(√1) + O(√2) + ... + O(√n) ---> approximately O(n^(3/2))
    def is_prime(k):
        for i in range(2, math.isqrt(k) + 1):
            if k % i == 0:
                return False

        return True
        
    @staticmethod
    def stream():
        yield 2
        yield 3
        n = 1
        while True:
            c1 = 6*n - 1
            c2 = 6*n + 1
            if Primes.is_prime(c1):
                yield c1
            if Primes.is_prime(c2):
                yield c2
            n += 1
            
