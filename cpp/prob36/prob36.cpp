#include <iostream>
#include <bitset>
#include <climits>
#include <string>
#include <chrono>

using namespace std;

string decToBin(int num)
{
    // convert to binary string (could just cout << the bitset, too)
    string bin = bitset<CHAR_BIT * sizeof(num)>(num).to_string();
    // trim leading zeroes
    bin = num ? bin.substr(bin.find('1')) : "0";
    return bin;
}

bool isPal(string num)
{
    int len = num.size();
    for (int i = 0; i < int(len/2); i++)
    { 
        if (num[i] != num[len-i-1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    auto start = chrono::high_resolution_clock::now();
    int max = 1000000;
    int sum = 0;

    for (int i = 1; i < max; i++)
    {
        if (isPal(to_string(i)) && isPal(decToBin(i)))
        {
            sum += i;
        }
    }

    cout << "sum of all palidromic numbers " << sum << endl;
    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
    return 0;
}