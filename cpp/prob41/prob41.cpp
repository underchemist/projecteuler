#include <iostream>
#include <string>
#include <chrono>
#include "../esieve.h"

bool isNPanDigital(std::string num_str)
{
    int len = num_str.size();
    for (auto it = num_str.begin(); it != num_str.end(); ++it)
    {
        auto temp = it;
        for (auto iit = ++temp; iit != num_str.end(); ++iit) {
            if (*it == *iit || *iit == '0' || *iit - '0' > len || *it - '0' > len) {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<int> primelist;
    int upperLimit = 7654321;
    eSieve(primelist, upperLimit);
    int max = 0;
    for (auto it = primelist.begin(); it != primelist.end(); ++it)
    {
        if (isNPanDigital(std::to_string(*it)))
        {
            if (max < *it)
            {
                max = *it;
            }
        }
    }
    std::cout << "largest pandigital prime is " << max << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}