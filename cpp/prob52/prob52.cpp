#include <iostream>
#include <chrono>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int result = 0;
    auto start = chrono::high_resolution_clock::now();
    for (int i = 10; i < 1000000; i++)
    {
        string digits = to_string(i);
        int number = i;
        int mult = 2;
        while (next_permutation(digits.begin(), digits.end()))
        {
            if (stoi(digits) == number*mult)
            {
                mult++;
                cout << digits << endl;
            }
        }
        if (mult == 7)
        {
            result = number;
            break;
        }
    }

    cout << "smallest positive integer with permuted multiples is " << result << endl;

    auto end = chrono::high_resolution_clock::now();
    cout << "time: " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
    return 0;
}