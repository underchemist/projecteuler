#include <iostream>
#include <string>
#include <chrono>

bool isPanDigital(std::string num_str)
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

std::string concatenate(int n)
{
    std::string concatenated;
    for (int j = 1; concatenated.size() < 9; j++)
    {
        concatenated.append(std::to_string(j*n));
    }
    return concatenated;
}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    int upperLimit = 98765; // think this is sufficient since next prod will have to be less than 9 with first
    int max = 0;
    for (int i = 1; i < upperLimit; i++)
    {
        std::string temp_str = concatenate(i);
        if (isPanDigital(temp_str))
        {
            int temp_int = std::stoi(temp_str);
            if (max < temp_int)
            {
                max = temp_int;
            }
        }
    }
    std::cout << "largest 1 to 9 pandigital number is " << max << std::endl;
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "time: " << std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count() << " ms" << std::endl;
    return 0;
}