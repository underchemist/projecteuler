#include <iostream>
#include <cmath>
#include <algorithm>
#include <chrono>
#include "../esieve.h"

int numPrimeFact(int n, std::vector<int>& primes)
{
    int nod = 0;
    int remain = n;
    bool pf;
    // since n always > 2 not much case checking
    for (size_t i = 0; i < primes.size(); i++) {
        // In case there is a remainder this is a prime factor as well
        // The exponent of that factor is 1
        if (primes[i] * primes[i] > n) {
            return ++nod;
        }
 
        pf = false;
        while (remain % primes[i] == 0) {
            pf = true;
            remain = remain / primes[i];
        }
        if (pf){
            nod++;
        }
 
        //If there is no remainder, return the count
        if (remain == 1) {
            return nod;
        }
    }
    return nod;
}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<int> primes;
    int upperLimit = 10000;
    eSieve::eSieve(primes, upperLimit);

    int i = 2*3*5*7;
    int consecutiveCount = 0;
    while (consecutiveCount < 4)
    {
        if (numPrimeFact(i,primes) >= 4)
        {
            consecutiveCount++;
        }
        else
        {
            consecutiveCount = 0;
        }
        i++;
    }

    std::cout << "the first of four consecutive with 4 distinct prime factors is " << i-4 << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}