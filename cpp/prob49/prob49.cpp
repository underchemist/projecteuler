#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <chrono>
#include "../esieve.h"

using namespace std;

int main()
{
    auto start = chrono::high_resolution_clock::now();
    int upperLimit = 10000;
    vector<int> primes = genESieve(upperLimit);
    auto startLimit = find(primes.begin(), primes.end(), 1009);
    vector<int> results;


    for (auto pit = startLimit; pit != primes.end(); ++pit)
    {;
        int first = *pit;
        string digits = to_string(*pit);
        vector<int> perms;
        perms.push_back(first);
        while (next_permutation(digits.begin(), digits.end()))
        {
            if (binary_search(startLimit, primes.end(), stoi(digits)))
            {
                perms.push_back(stoi(digits));
            }
        }
        for (auto iit = perms.begin(); iit != perms.end(); ++iit)
        {
            int dist = abs(first - *iit);
            auto check = iit;
            check++;
            while (check != perms.end())
            {
                if (abs(*iit - *check) == dist)
                {
                    results.push_back(first);
                    results.push_back(*iit);
                    results.push_back(*check);
                    break;
                }
                check++;
            }   
        }
    }
    cout << "prime permutations of equal distance are : " << endl;
    for (auto& it: results)
    {
        cout << it << " ";
    }
    cout << endl;

    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
    return 0;
}