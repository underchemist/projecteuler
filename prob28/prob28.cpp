/* Author: Yann-Sebastien Tremblay-Johnston
 * http://www.projecteuler.com attempt for problem 28 */

#include <iostream>
#include <chrono>
using namespace std;

int main() {
    auto start = chrono::high_resolution_clock::now();
    int sum = 1;
    int minisum = 1;
    int total = 1001*1001;
    int i, j;
    
    for (i = 2; minisum < total; i += 2) {
        for (j = 0; j < 4; j++) {
            minisum += i;
            sum += minisum;
        }
    }
    auto end = chrono::high_resolution_clock::now();
    cout << "The spiral sum should be: " << sum << endl;
    cout << "time: " << chrono::duration_cast<chrono::microseconds>(end-start).count() << " ms" << endl;
}
