#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <chrono>


int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    // generate pentagonal numbers
    std::vector<int> pentNums;
    pentNums.push_back(0);
    int max = 10000;
    for (int i = 1; i < max; i++)
    {
        pentNums.push_back(i*(3*i-1)/2);
    }
    int minDiff = pentNums[pentNums.size()-1] - pentNums[0];

    for (int j = 1; j < max; j++)
    {
        for (int k = 2; k < j; k++)
        {
            int pj = pentNums[j];
            int pk = pentNums[k];
            int sum = pj + pk;
            int diff = std::abs(pj - pk);
            if (std::binary_search(pentNums.begin(), pentNums.end(), sum) && std::binary_search(pentNums.begin(), pentNums.end(), diff))
            {
                if (minDiff > diff)
                {
                    minDiff = diff;
                }
            }
        }
    }
    std::cout << "minimum difference is " << minDiff << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}