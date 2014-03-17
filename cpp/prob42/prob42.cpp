#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>
#include <vector>
#include <map>
#include <chrono>

int calculateValue(std::string word, std::map<char, int>& mymap)
{
    int value = 0;
    for (char c: word)
    {
        value += mymap[c];
    }
    return value;
}

bool isTri(int value, std::vector<int>& triNums)
{
    if (*std::find(triNums.begin(), triNums.end(), value))
    {
        return true;
    }
    return false;
}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    // generate alphabet value map
    std::map<char, int> mymap;
    std::string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i = 1;
    for (char c: alphabet)
    {
        mymap[c] = i;
        i++;
    }

    // generate triangle numbers
    std::vector<int> triNums;
    int maxValue = 1000;
    int n = 1;
    int j = 1;
    while (n <= maxValue)
    {
        n = int(j*(j+1)/2);
        triNums.push_back(n);
        j++;
    }

    // find triangle words from words.txt
    int count = 0;
    std::string line;
    std::list<std::string> words;
    std::ifstream f("words.txt");
    std::getline(f, line);
    f.close();
    std::istringstream ss(line);
    while (ss)
    {
        std::string word;
        if (!getline( ss, word, ',' )) break;

        words.push_back(std::string(word, 1, word.length() - 2));
    }
    for (auto& it: words)
    {
        int value = calculateValue(it, mymap);
        if (isTri(value,triNums))
        {
            count++;
        }

    }
    std::cout << "there are " << count << " triangle words in 'words.txt'" << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::microseconds>(end-start).count() << " us" << std::endl;
    return 0;
}