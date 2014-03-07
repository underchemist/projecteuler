#include <iostream>
#include <cmath>
#include <chrono>

bool isWhole(double num) {
    return ceil(num) == floor(num);
}

unsigned long long calcTriNum(unsigned long long n)
{
    return n*(n+1)/2;
}

unsigned long long calcPentInd(unsigned long long triNum)
{
    double triNum_double = double(triNum);
    double root1 = double(1.0/6.0)*(1.0 + std::sqrt(1.0 + 24.0*triNum_double));
    double root2 = double(1.0/6.0)*(1.0 - std::sqrt(1.0 + 24.0*triNum_double));
    if (root1 > 0 && isWhole(root1))
    {
        return root1;
    }
    else if (root2 > 0 && isWhole(root2))
    {
        return root2;
    }
    else
    {
        return 0;
    }
}

unsigned long long calcHexInd(unsigned long long triNum)
{
    double triNum_double = double(triNum);
    double root1 = double(1.0/4.0)*(1.0 + std::sqrt(1.0 + 8.0*triNum_double));
    double root2 = double(1.0/4.0)*(1.0 - std::sqrt(1.0 + 8.0*triNum_double));
    if (root1 > 0 && isWhole(root1))
    {
        return root1;
    }
    else if (root2 > 0 && isWhole(root2))
    {
        return root2;
    }
    else
    {
        return 0;
    }
}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    unsigned long long i = 286;
    bool notfound = true;
    unsigned long long result = 0;
    while (notfound)
    {
        long triNum = calcTriNum(i);
        if (calcPentInd(triNum) && calcHexInd(triNum))
        {
            notfound = false;
            result = triNum;
        }
        i++;
    }
    std::cout << "the next number is " << result << std::endl;
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::microseconds>(end-start).count() << " us" << std::endl;
    return 0;
}