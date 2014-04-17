#include <iostream>
#include <cmath>
#include <chrono>

bool isinteger(double num) {
    return ceil(num) == floor(num);
}

int findside(int a, int b) {
    double c_doub = sqrt(a*a + b*b);
    if (isinteger(c_doub)) {
        return int(c_doub);
    }
    else {
        return 0;
    }
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    const int max = 10001;
    int a = 1, b = 1, c = 1;
    int i;
    int tempsum = 0;
    int p [max+1] = {0};
    int *ptr = &p[0];

    for (a = 1; a < max; a++) {
        for (b = 1; b < max; b++) {
            c = findside(a,b);
            if (c) {
                if (a+b+c > max) {
                    break;
                }
                tempsum = a + b + c;
                (*(ptr+tempsum))++;
            }
        }
    }

    int biggest = 0;
    int biggest_ind = 0;
    for (i = 1; i <= max ; i++) {
        std::cout << i << ": " << p[i] << std::endl;
        
        if (p[i] > biggest) {
            biggest = p[i];
            biggest_ind = i;
        }
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "value of p with largest number of solutions: " 
              << biggest_ind << std::endl;
    std::cout << "number of solution p has: "
              << int(biggest/2) << std::endl;
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}
