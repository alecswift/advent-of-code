#include <iostream>
#include <fstream>
#include <string>

int main() {
    int parse(std::string file_name);

    int sum = parse("/home/alec/Desktop/code/advent_of_code/2017/day_2/input.txt");

    std::cout << sum;

    return 0;
}

int parse(std::string file_name) {
    std::fstream in_file;
    std::string  data;
    int          min_max_diff(std::string line);
    int          sum;

    in_file.open(file_name, std::ios::in);
    if (!in_file) {
        std::cout << "no such file";
    } else {
        std::string line;

        while (!in_file.eof()) {
            std::getline (in_file, line);
            int diff = min_max_diff(line);
            sum += diff;
        }
    }
    in_file.close();

    return sum;
}

int min_max_diff(std::string line) {
    std::string temp;
    char        sep = '\t';
    int         maximum = 0;
    int         minimum = 0x0FFFFFFF;

    line += "\t";
    for (char ch : line) {
        if (ch == sep) {
            int num = std::stoi(temp);

            if (num > maximum) {
                maximum = num;
            }
            if (num < minimum) {
                minimum = num;
            }

            temp = "";
            continue;
        } 
        else {
            temp += ch;
        }
    }

    return maximum - minimum;
}

