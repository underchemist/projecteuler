from esieve3 import gen_primes
import numpy as np
from itertools import permutations

primes = gen_primes(int(1e7))

def eul_tot_fun(n):
    """
    Computes Euler's totient function as
    phi(n) = n * Prod(1 - 1/p)
    where p is a divisor of n
    """
    # find prime divisors
    pd = []
    for i in range(n//2):
        if n % primes[i] == 0:
            pd.append(primes[i])
    prime_divisors = np.array(pd)

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
    for n in range(2, int(1e3)):
        m = eul_tot_fun(n)
        if is_perm(n, m):
            res.append([n, n/m])
            print(n, n/m)
    print(np.array(res)[:, 1].min())

if __name__ == '__main__':
    main()
