#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

int sumOfFifthPows(int num)
{
    int power = 5;
    ostringstream convert;
    convert << num;
    string num_as_str = convert.str();
    int sum = 0;
    for (auto it = num_as_str.begin(); it != num_as_str.end(); ++it)
    {
        int digit = *it - '0';
        sum += int(pow(digit,power));
    } 
    return sum;
}

int main()
{
    int sum = 0;
    for (int i = 1; i < 590490*10; i++)
    {
        if (i == sumOfFifthPows(i))
        {
            sum += i;
        }
    }

    cout << sum << endl;
    return 0;
}