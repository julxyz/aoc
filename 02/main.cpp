#include "structs.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

pair<string, string> splitInTwo(string val) {
    string arg;
    string::size_type pos = val.find(' ');
    if(val.npos != pos) {
        arg = val.substr(pos + 1);
        val = val.substr(0, pos);
    }
    return make_pair(val, arg);
}

enum Direction {
    forward,
    down,
    up
};

Direction getDirection(string const& str) {
    if (str == "forward") return Direction::forward;
    if (str == "down") return Direction::down;
    if (str == "up") return Direction::up;
}

int main (int argc, char **argv) {
    std::string day(argv[1]);
    cout << "Solution for Day " << day << ":\n";

    int position = 0;
    int depth = 0; // same as aim
    int aimeddepth = 0;

    string line;
    ifstream input ((day + "/input.txt").c_str());
    if (input.is_open()) {
        while ( getline (input,line) ){
        // loop through input lines
        pair<string, string> args = splitInTwo(line);

        Direction d = getDirection(args.first);
        int amount = stoi(args.second);

        switch (d) {
            case Direction::forward:
                position += amount;
                aimeddepth += amount * depth;
                break;
            case Direction::down:
                depth += amount;
                break;
            case Direction::up:
                depth -= amount;
                break;
        }

        }
        input.close();
    }


    cout << "Horizontal position: " << position << "\nDepth without aim: " << depth << "\nDepth with aim: " << aimeddepth;
    cout << "\nFirst puzzle: " << position * depth;
    cout << "\nSecond puzzle: " << position * aimeddepth;
}