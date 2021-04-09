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
    return pow(e, -1, math.lcm((primes[0]-1),(primes[1]-1)))

if __name__ == "__main__":
    print(private_exponent(trial_division(int(sys.argv[1])), int(sys.argv[2])))