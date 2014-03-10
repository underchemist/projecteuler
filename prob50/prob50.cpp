#include <iostream>
#include <chrono>
#include <algorithm>
#include "../esieve.h"

using namespace std;

int main()
{
    auto start = chrono::high_resolution_clock::now();
    vector<int> primes = genESieve(1000000);
    vector<long> primeSum(primes.size()+1);
    primeSum[0] = 0;
    for (size_t i = 0; i < primes.size(); ++i)
    {
        primeSum[i+1] = primeSum[i] + primes[i];
    }

    int result = 0;
    int numPrimes = 0;
    int upperLimit = 0;
    for (size_t i = 0; i < primes.size(); ++i)
    {
        if (primeSum[i] > primes[primes.size()-1])
        {
            upperLimit = i-1;
            break;
        }
    }

    for (size_t i = upperLimit; i < primes.size() ; ++i)
    {
        for (size_t j = i - (numPrimes); j >= 1; --j)
        {
            if (primeSum[i] - primeSum[j] > primes[primes.size()-1]) break;
            if (binary_search(primes.begin(), primes.end(),primeSum[i] - primeSum[j]))
            {
                numPrimes = i-j;
                result = primeSum[i] - primeSum[j];
            }
        }
    }

    cout << "prime made of most consecutive prime numbers is " << result << endl;
    // cout << "which is made up of " << maxCount << " prime sums" << endl;
    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::microseconds>(end-start).count() << " us" << endl;
    return 0;
}