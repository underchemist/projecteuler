#include <iostream>
#include <algorithm>
#include <cmath>
#include <chrono>
#include "../esieve.h"

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    int upperLimit = 10000;
    std::vector<int> primes;
    eSieve(primes, upperLimit);
    int maxprime = primes[primes.size()-1];
    std::vector<int> oddComps(maxprime + 2*upperLimit*upperLimit+1, 0);

    for (auto& it: primes)
    {
        int i = 1;
        while (i < upperLimit)
        {
            oddComps[it + 2*(i*i)] = 1;
            i++;
        }
    }

    auto it = oddComps.begin();
    ++it;++it;
    std::cout << std::find(it ,oddComps.end(), 0) - oddComps.begin() << std::endl;
    for (size_t i = 0; i < oddComps.size(); i++)
    {
        auto ind = std::find(it, oddComps.end(), 0);
        int number = ind - oddComps.begin();
        if (number%2 && std::find(primes.begin(), primes.end(), number) == primes.end())
        {
            std::cout << "smallest odd composite not abiding Goldbach's conjecture is " << number
                      << std::endl;
            break;
        }
        it++;    
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}