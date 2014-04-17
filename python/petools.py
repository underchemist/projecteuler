from numpy import sqrt


class MRPrimeTest:

    def __init__(self):
        self._known_primes = [2, 3]

    def _try_composite(self, a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n  is definitely composite

    def is_prime(self, n, _precision_for_huge_n=16):
        if n in self._known_primes or n in (0, 1):
            return True
        if any((n % p) == 0 for p in self._known_primes):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        # Returns exact, according to http://primes.utm.edu/prove/prove2_3.html
        if n < 1373653:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 118670087467:
            if n == 3215031751:
                return False
            return (not any(self._try_composite(a, d, n, s)
                    for a in (2, 3, 5, 7)))
        if n < 2152302898747:
            return (not any(self._try_composite(a, d, n, s)
                    for a in (2, 3, 5, 7, 11)))
        if n < 3474749660383:
            return (not any(self._try_composite(a, d, n, s)
                    for a in (2, 3, 5, 7, 11, 13)))
        if n < 341550071728321:
            return (not any(self._try_composite(a, d, n, s)
                    for a in (2, 3, 5, 7, 11, 13, 17)))
        # otherwise
        return not any(self._try_composite(a, d, n, s)
                       for a in self._known_primes[:_precision_for_huge_n])


class ESieve(MRPrimeTest):
    def __init__(self):
        self = self

    def gen_primes(self, upperLimit):
        upperSqrt = int(sqrt(upperLimit)) + 1
        primes = []
        primeBools = [True] * (upperLimit + 1)
        primeBools[0] = False
        primeBools[1] = False

        for i in xrange(2, upperSqrt):
            if (primeBools[i]):
                primes.append(i)
                for j in xrange(i * i, upperLimit, i):
                    primeBools[j] = False

        for k in xrange(upperSqrt, upperLimit):
            if primeBools[k]:
                primes.append(k)

        return primes

    def gen_primes2(self, upperLimit):
        upperSqrt = int(sqrt(upperLimit)) + 1
        not_prime = set([0, 1])
        primes = []

        for i in xrange(2, upperSqrt):
            if i in not_prime:
                continue

            for j in xrange(i * i, upperLimit, i):
                not_prime.add(j)

            primes.extend(i)

        return primes
