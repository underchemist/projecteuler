#include <iostream>
#include <algorithm>
#include <chrono>

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    int num[] = {1,0,2,3,4,5,6,7,8,9};
    int divisors[] = {2,3,5,7,11,13,17};
    int numPerms = 3265920;
    int count = 0;
    long sum = 0;
    while (count < numPerms)
    {
        std::next_permutation(num,num+10);

        bool isDivisable = true;
        for (int k = 1; k < 8; k++) {

            int sub = 100 * num[k] + 10 * num[k + 1] + num[k + 2];
            if (sub % divisors[k-1] != 0) {
                isDivisable = false;
                break;
            }                    
        }
        if (isDivisable)
        {
            long temp = 0;
            for (int l = 0; l < 10; l++)
            {
                temp = 10*temp + num[l];
            }
            sum += temp;
        }
        count++;
    }
    std::cout << "sum of pandigital numbers with sub-string div is " << sum << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}