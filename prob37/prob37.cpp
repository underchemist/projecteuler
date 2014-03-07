#include <iostream>
#include <chrono>
#include <algorithm>
#include <string>
#include "../esieve.h"


bool isTruncatable(int p, std::vector<int>& primelist)
{
    std::string p_str = std::to_string(p);
    int len = p_str.size();

    if (p == 2 || p == 3 || p == 5 || p == 7)
    {
        return false;
    }

    // left to right and right to left
    for (int i = 0; i < len; i++)
    {
        std::string ltr_str = p_str.substr(i);
        std::string rtl_str = p_str.substr(0, len-i);
        int ltr_int = std::stoi(ltr_str);
        int rtl_int = std::stoi(rtl_str);
        if (!(std::binary_search(primelist.begin(),primelist.end(),ltr_int)))
        {
            return false;
        }
        else if (!(std::binary_search(primelist.begin(),primelist.end(),rtl_int)))
        {
            return false;
        }
    }
    return true;

}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    int max = 1000000; // guessing here with upper bound
    int sum = 0;
    std::vector<int> primelist;
    eSieve(primelist,max);
    
    // begin search for 11 truncatable primes
    int count = 0;
    for (size_t i = 1; i < primelist.size(); i++)
    {
        int p = primelist[i];
        if (count == 11)
        {
            break;
        }
        if (isTruncatable(p, primelist))
        {
            count++;
            sum += p;
        }
    }

    std::cout << "found " << count << " truncatable primes" << std::endl;
    std::cout << "the sum of them is " << sum << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() 
              << " ms" << std::endl;
    return 0;
}