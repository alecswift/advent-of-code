#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <vector>

int main() {
    std::vector<std::vector<std::string>> parse(std::string file_name);
    int count_valid_lists(std::vector<std::vector<std::string>> lines);
    int count_valid_lists_2(std::vector<std::vector<std::string>> lines);

    std::vector<std::vector<std::string>> lines;
    int                                   part_1;
    int                                   part_2;

    lines = parse("/home/alec/Desktop/code/advent_of_code/2017/day_4/input.txt");
    part_1 = count_valid_lists(lines);
    part_2 = count_valid_lists_2(lines);

    std::cout << part_1 << "\n" << part_2;

    return 0;
}

int count_valid_lists(std::vector<std::vector<std::string>> lines) {
    std::map<std::string, bool> unique_words;
    int                         count = 0;

    for (std::vector<std::string> words : lines) {
        
        for (std::string word : words) {
            unique_words[word] = true;
        }

        if (words.size() == unique_words.size()) {
            count++;
        }

        unique_words.clear();
    }

    return count;
}

int count_valid_lists_2(std::vector<std::vector<std::string>> lines) {
    int  has_pangram(std::vector<std::string> words);              
    int  count = 0;
    int  valid;

    for (std::vector<std::string> words : lines) {
        valid = has_pangram(words);
        count += valid;
    }

    return count;
}

int has_pangram(std::vector<std::string> words) {
    int idx_1 = 0;
    int idx_2;
    for (std::string word_1 : words) {
        idx_2 = 0;
        for (std::string word_2 : words) {
                
            //invalid change this (same words count as pangram)
            if (idx_1 == idx_2) {continue;}

            std::unordered_map<char, int> chars_1;
            std::unordered_map<char, int> chars_2;

            for (int idx = 0; idx < word_1.size(); idx++) {
                if (!chars_1.count(word_1[idx])) {
                    chars_1[word_1[idx]] = 1;
                } else {
                    chars_1[word_1[idx]] += 1;
                }
                
                if (!chars_2.count(word_2[idx])) {
                    chars_2[word_2[idx]] = 1;
                } else {
                    chars_2[word_2[idx]] += 1;
                }
            }

            if (chars_1 == chars_2) {
                return 0;
            }

            idx_2++;
        }

        idx_1++;
    }
    return 1;
}

std::vector<std::vector<std::string>> parse(std::string file_name) {

    std::fstream                          in_file;
    std::vector<std::string>              words;
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