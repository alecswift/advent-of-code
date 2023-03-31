#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::vector<std::string>> parse(std::string file_name);

    std::vector<std::vector<std::string>> lines;

    lines = parse("/home/alec/Desktop/code/advent_of_code/2017/day_4/input.txt");

    return 0;
}

std::vector<std::vector<std::string>> parse(std::string file_name) {

    std::fstream                          in_file;
    std::vector<std::string>                      words;
    std::vector<std::vector<std::string>> lines;

    std::vector<std::string> build_words(std::string line);

    in_file.open(file_name, std::ios::in);

    if (!in_file) {
        std::cout << "No such file";
    } else {
        std::string line;

        while (std::getline (in_file, line)) {
            words = build_words(line);
            lines.push_back(words);
        }
    }

    return lines;
}

std::vector<std::string> build_words(std::string line) {
    std::string      temp;
    char             sep = ' ';
    std::vector<std::string> words;

    line += " ";
    for (char ch : line) {
        if (ch == sep) {
            words.push_back(temp);
            temp = "";
            continue;
        } 
        else {
            temp += ch;
        }
    }

    return words;
}