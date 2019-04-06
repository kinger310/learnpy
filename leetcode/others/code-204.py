# 204. Count Primes
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


def countPrimes(n: int) -> int:
    if n < 3:
        return 0
    prime = [True] * n
    prime[0] = prime[1] = False
    i = 2
    while i * i <= n:
        if prime[i]:
            prime[i*i:n:i] = [False]*len(prime[i*i:n:i])
        i += 1
    return sum(prime)

print(countPrimes(25))