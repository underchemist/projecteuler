/* basic implementation of sieve of Eratosthenes
 * using example from http://www.mathblog.dk/
 * will generate a vector of primes up to a 
 * certain limit */

#ifndef __ESIEVE_H__
#define __ESIEVE_H__

#include <cmath>
#include <vector>

std::vector<int> genESieve(int upperLimit) {
    int upperSqrt = int(std::sqrt(double(upperLimit)));
    std::vector<int> primes;
    std::vector<bool> primeBools(int(upperLimit+1));
    // bool *PrimeBools = new bool[(int)upperLimit+1]();
    primeBools[0] = 0;
    primeBools[1] = 0;

    for (int i = 2; i <= upperSqrt; i++) {
        if (!primeBools[i]) {
            for (int j = i * i; j <= upperLimit; j += i) {
                primeBools[j] = 1;
            }
        }
    }
 
    for (int i = 2; i <= upperLimit; i++) {
        if (!primeBools[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}

#endif
