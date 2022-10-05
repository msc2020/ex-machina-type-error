# BlueBook code decryption

import time

import sys

def sieve(n):
# Compute primes using sieve of Eratosthenes
    
    x = [1]*n
    x[1] = 0

    #for i in range(2, n/2): # raise an error
    for i in range(2, n//2): # iterate on integers
        j = 2*i
        while j < n:
            x[j] = 0 
            j = j+1
    return x


n = 10
print(sieve(n))
#time.sleep(3)

# https://en.wikipedia.org/wiki/Deus_ex_machina
