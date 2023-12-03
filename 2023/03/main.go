package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

var input []string
var filter = regexp.MustCompile(`[^0-9.]+`)
var number = regexp.MustCompile(`[0-9]`)

func main() {
	// read input
	readFile, err := os.Open("input.txt")
	checkErr(err)
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
	}
	readFile.Close()

	// All

	// First
	{
		sum := 0
		for i, line := range input {
			for j := 0; j < len(line); j++ {
				width := 0
				for number.MatchString(string(line[j])) {
					width++
					j++
					if j == 140 {
						break
					}
				}
				if width > 0 {
					if searchOne(j-width, i, width) {
						partNum, err := strconv.Atoi(line[j-width : j])
						checkErr(err)
						sum += partNum
					}
				}
			}
		}
		fmt.Println(sum)
	}
	// Second
	{
		sum := 0
		for i, line := range input {
			for j := 0; j < len(line); j++ {
				if string(line[j]) == "*" {
					numbers := searchTwo(j, i)
					if numbers == 2 {
						sum += ratio(j, i)
					}
				}
			}
		}
		fmt.Println(sum)
	}

}

func searchOne(x int, y int, width int) bool {
	// fmt.Println("---------------")
	for y_var := y - 1; y_var <= y+1; y_var++ {
		if y_var < 0 || y_var > 139 {
			continue
		}
		for x_var := x - 1; x_var <= x+width; x_var++ {
			if x_var < 0 || x_var > 139 {
				continue
			}
			// fmt.Print(string(input[y_var][x_var]))
			if filter.MatchString(string(input[y_var][x_var])) {
				// fmt.Println("bling")
				return true
			}
		}
	}
	return false
}

func searchTwo(x int, y int) int {
	m := [3][3]bool{}
	y_m := 0
	for y_var := y - 1; y_var <= y+1; y_var++ {
		x_m := 0
		if y_var < 0 || y_var > 139 {
			continue
		}
		for x_var := x - 1; x_var <= x+1; x_var++ {
			if x_var < 0 || x_var > 139 {
				continue
			}
			if number.MatchString(string(input[y_var][x_var])) {
				m[y_m][x_m] = true
			}
			x_m++
		}
		y_m++
	}

	return countNums(m)
}

func countNums(m [3][3]bool) (res int) {
	for _, r := range m {
		if r[0] {
			res++
			if r[2] && !r[1] {
				res++
			}
		} else if r[1] || r[2] {
			res++
		}
	}
	return
}

func ratio(x int, y int) int {
	a, b := 0, 0
	for y_var := y - 1; y_var <= y+1; y_var++ {
		if y_var < 0 || y_var > 139 {
			continue
		}
		for x_var := x - 1; x_var <= x+1; x_var++ {
			if x_var < 0 || x_var > 139 {
				continue
			}
			if number.MatchString(string(input[y_var][x_var])) {
				left := leftTrace(x_var, y_var)
				right := rightTrace(x_var, y_var)
				a, b = assign(a, b, input[y_var][x_var-left:x_var+right+1])
				x_var += right
			}
		}
	}

	return a * b
}

func leftTrace(x int, y int) (res int) {
	for x > 0 {
		x--
		if number.MatchString(string(input[y][x])) {
			res++
		} else {
			break
		}
	}
	return
}
func rightTrace(x int, y int) (res int) {
	for x < 139 {
		x++
		if number.MatchString(string(input[y][x])) {
			res++
		} else {
			break
		}
	}
	return
}

func assign(a int, b int, s string) (int, int) {
	val, err := strconv.Atoi(s)
	checkErr(err)
	if a == 0 {
		a = val
	} else {
		b = val
	}
	return a, b

}
