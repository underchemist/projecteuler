#include <iostream>
#include <chrono>
#include <algorithm>
#include "../esieve.h"

using namespace std;

int main()
{
    auto start = chrono::high_resolution_clock::now();
    vector<int> primes = genESieve(1000000);

    for (auto it: primes)
    {
        string digits = to_string(it);
        int count = 0;
        for (size_t digits_to_replace = 1; digits_to_replace < digits.size(); digits_to_replace++)
        {
            for ()
        }
    }

    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
    return 0;
}