"""
A simple implementation of the Sieve of Eratosthenes in python. Should return
an array based on a predefined upper limit.
"""


def gen_primes(upperLimit):
    upperSqrt = int((upperLimit)**0.5) + 1
    primes = []
    primeBools = [True] * (upperLimit + 1)
    primeBools[0] = False
    primeBools[1] = False

    for i in range(2, upperSqrt):
        if (primeBools[i]):
            primes.append(i)
            for j in range(i * i, upperLimit, i):
                primeBools[j] = False

    for k in range(upperSqrt, upperLimit):
        if primeBools[k]:
            primes.append(k)

    return primes

if __name__ == "__main__":
    import sys

    try:
        if len(sys.argv) <= 2:
            upperLimit = int(sys.argv[1])
            print(gen_primes(upperLimit))
    except TypeError or IndexError:
        print("USAGE: python esieve.py INT")
