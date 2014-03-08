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
 
    bool *PrimeBools = new bool[(int)upperLimit+1]();
    PrimeBools[0] = 0;
    PrimeBools[1] = 0;

    for (int i = 2; i <= upperSqrt; i++) {
        if (!PrimeBools[i]) {
            for (int j = i * i; j <= upperLimit; j += i) {
                PrimeBools[j] = 1;
            }
        }
    }
 
    for (int i = 2; i <= upperLimit; i++) {
        if (!PrimeBools[i]) {
            primes.push_back(i);
        }
    }
    delete [] PrimeBools;
    return primes;
}

#endif
