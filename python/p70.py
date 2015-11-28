from esieve3 import gen_primes
import numpy as np
from itertools import permutations

primes = gen_primes(int(1e7))
not_primes = np.setdiff1d(np.arange(2, int(1e4), 1), primes)

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

def pfactors(n):
    """
    computes prime factors of n, still naive with small optimization
    """
    pd = []
    lim = int(np.sqrt(n))
    if n % 2 == 0:
        pd.append(2)
        while n % 2 == 0:
            n = n/2
    for p in primes[1:]:
        if n % p == 0:
            pd.append(p)
            while n % p == 0:
                n = n/p
        if n == 1:
            break
        if p > lim:
            pd.append(int(n))
            break
    return np.array(pd)


def eul_tot_fun(n):
    """
    Computes Euler's totient function as
    phi(n) = n * Prod(1 - 1/p)
    where p is a divisor of n
    """
    # find prime divisors
    pd = []
    lim = np.sqrt(n)
    for i in range(n//2):
        if n % primes[i] == 0:
            pd.append(primes[i])

    prime_divisors = np.array(pd)

    return int(n * (1-1/prime_divisors).prod())

def eul_tot_fun2(n):
    """
    Computes Euler's totient function as
    phi(n) = n * Prod(1 - 1/p)
    where p is a divisor of n
    """
    prime_divisors = pfactors(n)

    return int(n * (1-1/prime_divisors).prod())

def tuple_to_int(t):
    return int(''.join(str(T) for T in t))

def is_perm(n, m):
    """
    determine if m is a cyclic permutation of n
    """
    n_str = str(n)
    for perm in permutations(n_str):
        if tuple_to_int(perm) == m:
            return True

    return False

def main():
    res = []
    for n in not_primes:
        m = eul_tot_fun2(n)
        if is_perm(n, m):
            res.append([n, n/m])
    res = np.array(res)
    print(res[res[:, 1].argmin(), 0], res[:, 1].min())

def main2():
    res = []
    for n in not_primes:
        m = eul_tot_fun2(n)
        n_str = str(n)
        m_str = str(m)
        if len(m_str) == len(n_str):
            if sorted(n_str) == sorted(m_str):
                res.append([n, n/m])
    res = np.array(res)
    print(res[res[:, 1].argmin(), 0], res[:, 1].min())


if __name__ == '__main__':
    pass
