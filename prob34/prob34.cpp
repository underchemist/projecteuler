#include <iostream>
#include <boost/math/special_functions/factorials.hpp>
#include <string>
#include <chrono>

using namespace std;
using namespace boost::math;

string numToString(int n) 
{
    string str = to_string(factorial<float>(n));
    return str;
}

int main() 
{
    cout << numToString(4) << endl;
	return 0;
}