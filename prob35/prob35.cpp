#include <iostream>
#include <string>
#include <algorithm>
#include "../esieve.h"

void perm(int& p, int check = 1)
{
    if (check)
    {
        int p_temp = p;
        string p_str = to_string(p_temp);
        string p_new;
        char first_digit = p_str[0];
        for (size_t i = 1; i < p_str.size(); i++)
        {
            p_new.push_back(p_str[i]);
        }
        p_new.push_back(first_digit);
        p = stoi(p_new);
    }
    else
    {
        int p_temp = p;
        string p_new = to_string(p_temp);
        p_new.push_back('0');
        p = stoi(p_new);
    }
}

int main()
{
    int max = 1000000;
    vector<int> primelist;
    eSieve(primelist, max);
    int count = 0;
    for (size_t j = 0; j < primelist.size(); j++)
    {
        int p = primelist[j];
        string original = to_string(p);
        size_t len = original.size();
        perm(p);
        string current = to_string(p);
        while (current != original)
        {
            int check = 1;
            if (current.size() != len)
            {
                check = 0;
            }
            if (*(find(primelist.begin(),primelist.end(),p)) == *primelist.end())
            {
                break;
            }
            perm(p,check);
            current = to_string(p);
        }
        if (current == original)
        {
            count++;
            cout << p << endl;
        }
    }
    cout << "there are "<< count << " circular primes" << endl;
    return 0;
}