#include <iostream>
#include <algorithm>
#include <cmath>
#include <list>

using namespace std;

int main() 
{
    list<double> set;
    double result;
    for (int a = 2; a <= 100; a++)
    {
        for ( int b = 2; b <= 100; b++)
        {
            result = pow(a,b);

            if ((find(set.begin(),set.end(), result)) == set.end())
            {
                set.push_back(result);
            }
        }
    }
    cout << "number of distint powers is " << set.size() << endl;
    cout << pow(100,100) << endl;
}