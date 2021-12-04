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
    if (input.is_open()) {
        while ( getline (input,line) ){
        
        // loop through input lines

        }
        input.close();
    }
}