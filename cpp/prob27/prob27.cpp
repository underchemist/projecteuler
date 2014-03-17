#include <iostream>
#include <chrono>
#include <algorithm>
#include "esieve.h"

using namespace std;

int primeQuad(int n, int a, int b)
{
    return n*n + a*n + b;
}

int main()
{
    auto start = chrono::high_resolution_clock::now();
    int max = 87400;
    int prime_streak = 0;
    vector<int> primelist;
    eSieve(primelist, max);

    for (int i = -1000; i < 1000; i++)
    {
        for (int j = -i; j < 1000; j++)
        {
            int n = 0;
            while (*find(primelist.begin(),primelist.end(),primeQuad(n,i,j)))
            {
                ++n;
                if (n > prime_streak)
                {
                    prime_streak = n;
                    cout << "a: " << i << " b: " << j << ", " << prime_streak << endl;
                }
            }
        }
    }

    cout << "largest number of consecutive primes produces was " << prime_streak << endl;
    auto end = chrono::high_resolution_clock::now();
    cout << endl << "time: " << chrono::duration_cast<chrono::microseconds>(end-start).count()
         << " us" << endl;
    return 0;
}