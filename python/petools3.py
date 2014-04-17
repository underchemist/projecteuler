from bitarray import bitarray


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
        """ slightly faster for primes larger than 10 000 000 """
        upperSqrt = int(upperLimit ** 0.5)
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

    def gen_primes2(self, upperLimit):
        """ slowest at the moment """
        upperSqrt = int(upperLimit ** 0.5) + 1
        s = set(range(upperLimit + 1))
        primeBools = dict.fromkeys(s, True)
        primeBools[0], primeBools[1] = False, False
        primes = []

        for i in range(2, upperSqrt):
            if (primeBools[i]):
                primes.append(i)
                for j in range(i * i, upperLimit, i):
                    primeBools[j] = False

        for k in range(upperSqrt, upperLimit):
            if primeBools[k]:
                primes.append(k)

        return primes

    def gen_primes3(self, n):
        """ fastest below 10 000 000 but blows up past that """
        size = n // 2
        sieve = [1] * size
        limit = int(n ** 0.5)
        for i in range(1, limit):
            if sieve[i]:
                val = 2 * i + 1
                tmp = ((size - 1) - i) // val
                sieve[i + val::val] = [0] * tmp
        return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]

    def gen_primes4(self, upperLimit):
        primeBools = bitarray(upperLimit // 2)
        primeBools.setall(True)
        primeBools[0] = False
        upperSqrt = int(upperLimit ** 0.5)

        i = 3
        while i < upperSqrt:
            primeBools[i * i // 2: upperLimit // 2: i] = False
            i = (primeBools.index(True, i // 2 + 1)) * 2 + 1

        return [2] + [j * 2 + 1 for j, v in enumerate(primeBools) if v and j > 0]
