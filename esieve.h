#ifndef __ESIEVE_H__
#define __ESIEVE_H__

#include <cmath>
#include <vector>

using namespace std;

void eSieve(vector<int>& primelist, int upperLimit) {
    int upperSqrt = ((int)sqrt((double)upperLimit));
 
    bool *PrimeBools = new bool[(int)upperLimit+1]();
    PrimeBools[0] = 0;
    PrimeBools[1] = 0;

    for (int i = 2; i <= upperSqrt; i++) {
        if (!PrimeBools[i]) {
            for (int j = i * i; j <= upperLimit; j += i) {
                PrimeBools[j] = 1;
            }
        }
    }
 
    for (int i = 1; i <= upperLimit; i++) {
        if (!PrimeBools[i]) {
            primelist.push_back(i);
        }
    }
    delete [] PrimeBools;
}

#endif