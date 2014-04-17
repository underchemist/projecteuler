#include <iostream>
#include <list>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

bool isPanDigital(string num_str)
{
    for (auto it = num_str.begin(); it != num_str.end(); ++it)
    {
        auto temp = it;
        for (auto iit = ++temp; iit != num_str.end(); ++iit) {
            if (*it == *iit || *iit == '0') {
                return false;
            }
        }
    }

    return true;
}

int main() {
    list<int> set;
    int sum = 0;
    for (int a = 1; a < 9876; a++) {
        for (int b = 1; b < a; b++) {
            int prod = a*b;
            string num_str = to_string(a) + to_string(b) + to_string(prod);

            if (num_str.size() != 9) {
                continue;
            }

            if (isPanDigital(num_str)) {
                cout << a << " " << b << " " << prod  << endl;
                if (find(set.begin(), set.end(), prod) == set.end()) {
                    set.push_back(prod);
                    sum += prod;
                }
            }
        }
    }
    cout << sum << endl;
    return 0;
}
