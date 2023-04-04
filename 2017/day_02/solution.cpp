// Puzzle explanation: https://adventofcode.com/2017/day/2

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    std::vector<int> part_1(std::string file_name);
    int part_2_diff(std::string line);

    std::vector<int> solutions = part_1("/home/alec/Desktop/code/advent_of_code/2017/day_2/input.txt");
    int x = part_2_diff("798	1976	1866	1862	559	1797	1129	747	85	1108	104	2000	248	131	87	95");

    std::cout << solutions[0] << "\n";
    std::cout << solutions[1];

    return 0;
}

std::vector<int> part_1(std::string file_name) {
    std::fstream     in_file;
    std::string      data;
    std::vector<int> solutions;
    int              sum;
    int              sum_2;
    int              min_max_diff(std::string line);
    int              part_2_diff(std::string line);

    in_file.open(file_name, std::ios::in);
    if (!in_file) {
        std::cout << "no such file";
    } else {
        std::string line;

        while (std::getline (in_file, line)) {
            int diff = min_max_diff(line);
            sum += diff;
        }

        in_file.clear();
        in_file.seekg(0, in_file.beg);

        while (std::getline (in_file, line)) {
            int diff_2 = part_2_diff(line);
            sum_2 += diff_2;

        }
    }
    in_file.close();

    solutions.push_back(sum);
    solutions.push_back(sum_2);
    return solutions;
}

int part_2_diff(std::string line) {
    std::vector<int> row;
    std::string temp;
    char        sep = '\t';

    line += "\t";
    for (char ch : line) {
        if (ch == sep) {
            int num = std::stoi(temp);
            row.push_back(num);
            temp = "";
            continue;
        } 
        else {
            temp += ch;
        }
    }
    
    for (int idx = 0; idx < row.size(); idx++) {
        int num = row[idx];

        for (int idx_2 = 0; idx_2 < row.size(); idx_2++) {
            int num_2 = row[idx_2];

            if (num != num_2 && num % num_2 == 0) {
                return num / num_2;
            }
        }
    }

    return -1;
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

