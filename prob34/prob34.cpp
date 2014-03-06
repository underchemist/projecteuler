#include <iostream>
#include <boost/math/special_functions/factorials.hpp>
#include <string>
#include <chrono>

using namespace std;
using namespace boost::math;

double fact(int n) 
{
    return factorial<double>(n);
}

int main() 
{
    auto start = chrono::high_resolution_clock::now();
    int sum = 0;
    for (int i = 10; i < 999999; i++)
    {
        string str = to_string(i);
        int temp_sum = 0;
        for (auto it = str.begin(); it != str.end(); ++it)
        {  
            int temp_digit = *it - '0'; // there should be a better way to do this ...
            temp_sum += int(fact(temp_digit));
        }
        if (temp_sum == i)
        {
            sum += i;
        }
    }

    cout << "sum of all numbers which are equal to factorial digits: " << sum << endl;
    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
	
    return 0;
}