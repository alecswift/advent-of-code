// Puzzle explanation: https://adventofcode.com/2017/day/1

#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::string parse(std::string input_file);
    int count_rep_chars(std::string data);

    std::string data = parse("/home/alec/Desktop/code/advent_of_code/2017/day_1/solution.cpp");
    int count1 = count_rep_chars(data);
    std::cout << count1;
    return 0;
}

std::string parse(std::string input_file) {
    std::fstream my_file;
    std::string  data;

    my_file.open("/home/alec/Desktop/code/advent_of_code/2017/day_1/input.txt", std::ios::in);
    if (!my_file) {
        std::cout << "no such file";
    } else {
        char ch;

        while (1) {
            my_file >> ch;
            if (my_file.eof()) {
                break;
            }
            data += ch;
        }

    }

    my_file.close();
    return data;
}

int count_rep_chars(std::string data) {
    int count = 0;

    for (int idx = 0; idx < data.length(); idx++) {
        int next_idx = (idx + 1) % data.length();
        char ch = data[idx];

        if (ch == data[next_idx]) {
            int num = ch - '0';
            count += num;
        }
    }

    return count;
}