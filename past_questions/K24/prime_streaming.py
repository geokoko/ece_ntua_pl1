import math
class Primes:
    @staticmethod
    # Time Complexity: O(sqrt(k))
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

    # Adding print_primes method to print the first N prime numbers here:
    def print_primes(N, M):
        count = 1
        for prime in Primes.stream():
            if count >= N and count <= M:
                print(prime)
            count += 1
            if count > M: # Loop stops when count exceeds M, so complexity is O(M*)
                break

Primes.print_primes(1, 9)

# Time Complexity explanation:
# The prime number theorem states that the number of primes up to any number K is approximately K/log(K). 
# So, to find the first M primes, we need M = K/log(K) => K = M*log(K)            
# To check if a number K is prime, we need to check if it is divisible by any number up to sqrt(K). So, complexity of O(sqrt(K)) for every K.
# This means that the overall complexity is the sum  O(√1) + O(√2) + ... + O(√K) ---> approximately O(K^(3/2)) for searching up to number K.
# But K = M*log(K) => O((M*log(K))^(3/2)) = O(M^(3/2) * log(K)^(3/2))


