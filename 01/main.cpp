#include "structs.h"
#include <algorithm>
#include <iostream>
#include <list>
#include <fstream>
#include <iterator>
#include <string>
using namespace std;

int main (int argc, char **argv) {
    std::string day(argv[1]);
    cout << "Solution for Day " << day << ":\n";

    //read input
    string line;
    ifstream input ((day + "/input.txt").c_str());
    std::list<int> measurements = {};

    if (input.is_open()) {
        while ( getline (input,line) ){
            int x = stoi(line);
            measurements.push_back(x);
        }
        input.close();
    }

    int prevValue = 10000; //value of previous measurement
    int firstResult = 0; //number of measurements larger than previous measurement

    for (int currentValue : measurements) {
        //increment i if current measurement is larger than previous value
        if (currentValue > prevValue) {
            firstResult++;
        }
        //set previous measurement to current value for next iteration
        prevValue = currentValue;
    }

    cout << "First Puzzle: " << firstResult << "\n";

    int secondResult = 0; //number of measurement windows larger than previous window

    //set up initial measurement windows
    auto cursor = measurements.begin(); //cursor adding new measurement at the front of the next window
    auto follower = cursor; //follower cursor removing last measurement from the next window
    int prevWindow = *cursor;
    advance(cursor, 1);
    prevWindow += *cursor;
    advance(cursor, 1);
    prevWindow += *cursor;
    int nextWindow = prevWindow;

    for (int i = 3; i<2000; i++) {
        //calculate next window sum
        advance(cursor, 1);
        nextWindow -= *follower;
        nextWindow += *cursor;
        advance(follower, 1);

        //compare windows
        if (nextWindow>prevWindow) {
            secondResult++;
        }
        //set previous window to current window
        prevWindow = nextWindow;
    }

    
    cout << "Second Puzzle: " << secondResult << "\n";
}