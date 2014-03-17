#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(void) {
    int sequenceLength = 0;
    int num = 0;
     
    for (int i = 1000; i > 1; i--) {
        if (sequenceLength >= i) {
            break;
        }
     
        vector<int> foundRemainders(i,0);
        int value = 1;
        int position = 0;
     
        while (foundRemainders[value] == 0 && value != 0) {
            foundRemainders[value] = position;
            value *= 10;
            value %= i;
            position++;
        }
     
        if (position - foundRemainders[value] > sequenceLength) {
            num = i;
            sequenceLength = position - foundRemainders[value];
        }
    }
    printf("number with longest cycle is %d and cycle length is %d", num, sequenceLength);
}
