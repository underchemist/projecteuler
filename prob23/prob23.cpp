#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <list>
#include <chrono>

using namespace std;

int sumOfFactorsPrime(int number, vector<int>& primelist, int length) {
    int n = number;
    int sum = 1;
    int p = primelist[1];
    int j;
    int i = 1; 
 
    while (p * p <= n && n > 1 && i < length) {
        p = primelist[i];
        i++;
        if (n % p == 0) {
            j = p * p;
            n = n / p;
            while (n % p == 0) {
                j = j * p;
                n = n / p;
            }
            sum = sum * (j - 1) / (p - 1);
        }
    }
 
    //A prime factor larger than the square root remains
    if (n > 1) {
        sum *= n + 1;
    }
    return sum - number;
}

void ESieve(vector<int>& primelist, int upperLimit) {
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

//bool isAbun(int N) {
//    int d = N;
//    int sum = 0;
//
//    while (--d > 0) {
//        if ((N % d) == 0) {
//           sum += d;
//        }
//    }
//
//    if (sum <= N) {
//        return false;
//    }
//    else {
//        return true;
//    }
//}
//
void printToFile(vector<int>& V) {
    unsigned int i;

    ofstream myfile;
    myfile.open("nonAbundantNumbers.txt");
    
    for (i = 0; i < V.size(); i++) {
        myfile << V[i] << endl;
    }
    myfile.close();
}

int main() {
    auto start = chrono::high_resolution_clock::now();
    const int max = 28123;
    unsigned int i,j;
    int k;
    vector<int> sum_ind(max+1,0);
    vector<int> Abuns;
    vector<int> primelist;
    ESieve(primelist, max);
    long sum = 0;
    int length = primelist.size(); 
    
    printToFile(primelist);
    // Find abundant numbers
    for (k = 1; k <= max; k++) {
        if (sumOfFactorsPrime(k, primelist, length) > k) {
            Abuns.push_back(k);
        }
    }

    // Sum abundant numbers in a unique way?
    for (i = 0; i < Abuns.size(); i++) {
        for (j = i; j < Abuns.size(); j++) {
            if (Abuns[i] + Abuns[j] <= max) {
                sum_ind[Abuns[i] + Abuns[j]] = 1;
            }
            else {
                break;
            }
        }
    }


    for (k = 1; k <= max; k++) {
        if (!sum_ind[k]) {
            sum += k;
        }
    }
    cout << "Sum: " << sum << endl;
    auto end = chrono::high_resolution_clock::now();
    cout << "Time took was " << chrono::duration_cast<chrono::milliseconds>(end-start).count() << " ms" << endl;
}
