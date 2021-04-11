import sys
import math

def trial_division(n):
    i = 3
    lim = int(n/2)
    while i < lim:
        #print(f"{i} / {lim}", end='\r')
        if (n % i == 0):
            return (i, int(n/i))
        i += 2


def private_exponent(primes, e):
    """ Find RSA private exponent e given primes p and q """ 
    return pow(e, -1, math.lcm((primes[0]-1),(primes[1]-1)))

# fast prime generator from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def prime_division(n):
    """ Checks n divisibilty by list of primes in order from sqrt(n) to 2 """
    primes = primes1(int(math.sqrt(n)))
    for prime in reversed(primes):
        if n % prime == 0:
            print((prime, int(n/prime)))
            return (prime, int(n/prime))

if __name__ == "__main__":
    if sys.argv[1] == "-t":
        print(private_exponent(trial_division(int(sys.argv[2])), int(sys.argv[3])))
    elif sys.argv[1] == "-p":
        print(private_exponent(prime_division(int(sys.argv[2])), int(sys.argv[3])))