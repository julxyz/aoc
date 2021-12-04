#include "structs.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char **argv) {
    std::string day(argv[1]);
    cout << "Solution for Day " << day << ":\n";

    string line;
    ifstream input ((day + "/input.txt").c_str());

    
    int prev = 10000; //value of previous measurement
    int i = 0; //number of measurements larger than previous measurement

    if (input.is_open()) {
        while ( getline (input,line) ){
            int current = stoi(line);

            //increment i if current measurement is larger than previous value
            if (current > prev) {
                i++;
            }

            //set previous measurement to current value for next iteration
            prev = current;
        }
        input.close();
    }
    cout << "First Puzzle:" << i;
}