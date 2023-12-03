package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	// read input
	readFile, err := os.Open("input.txt")
	checkErr(err)
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var input []string
	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
	}
	readFile.Close()

	// All
	regex := regexp.MustCompile(`[^1-9 ]+`)

	// First
	{
		sum := 0

		for _, line := range input {
			nums := regex.ReplaceAllString(line, "")
			value, _ := strconv.Atoi(nums[0:1] + nums[len(nums)-1:])
			sum += value
		}
		fmt.Println(sum)
	}
	// Second
	{
		notchangingmysolution := strings.NewReplacer("oneight", "18", "twone", "21", "threeight", "38", "fiveight", "58", "sevenine", "79", "nineight", "98", "eightwo", "82")
		r := strings.NewReplacer("one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9")
		sum := 0

		for _, line := range input {
			l := notchangingmysolution.Replace(line)
			l = r.Replace(l)
			nums := regex.ReplaceAllString(l, "")
			value, err := strconv.Atoi(nums[0:1] + nums[len(nums)-1:])
			checkErr(err)
			sum += value
		}
		fmt.Println(sum)
	}
}
