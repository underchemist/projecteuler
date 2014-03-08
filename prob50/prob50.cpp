#include <iostream>
#include <chrono>
#include <algorithm>
#include "../esieve.h"

using namespace std;

int main()
{
    auto start = chrono::high_resolution_clock::now();
    vector<int> primes = genESieve(1000000);
    int result = 0;
    int maxCount = 0;
    for (size_t i = 0; i < primes.size(); i++)
    {
        int count = 0;
        int sum = primes[i];
        for (size_t j = i+1; j < primes.size(); i++)
        {
            sum += primes[j];
            if (binary_search(primes.begin(),primes.end(), sum))
            {
                count++;
            }   
            else
            {
                break;
            }
        }
        if (maxCount < count)
        {
            maxCount = count;
            result = sum;
        }
    }
    cout << "prime made of most consecutive prime numbers is " << result << endl;
    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
    return 0;
}