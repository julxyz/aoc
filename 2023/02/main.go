package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

type Set struct {
	Red   int
	Blue  int
	Green int
}

type Game struct {
	ID   int
	Sets []Set
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
	var games []Game
	for _, line := range input {
		var game Game
		split := strings.Split(line, ": ")
		game.ID, err = strconv.Atoi(strings.Split(split[0], " ")[1])
		checkErr(err)
		sets := strings.Split(split[1], "; ")
		for _, s := range sets {
			var set Set
			colors := strings.Split(s, ", ")
			for _, c := range colors {
				color := strings.Split(c, " ")
				amount, err := strconv.Atoi(color[0])
				checkErr(err)
				switch color[1] {
				case "green":
					set.Green = amount
				case "red":
					set.Red = amount
				case "blue":
					set.Blue = amount
				}

			}
			game.Sets = append(game.Sets, set)
		}
		games = append(games, game)
	}

	// First
	{
		sum := 0
		t := Set{Red: 12, Green: 13, Blue: 14}
		for _, g := range games {
			p := true
			for _, s := range g.Sets {
				sp := possible(s, t)
				if !sp {
					p = false
				}
			}
			if p {
				sum += g.ID
			}
		}
		fmt.Println(sum)
	}
	// Second
	{
		sum := 0
		for _, g := range games {
			min := minSet(g.Sets)
			sum += power(min)
		}
		fmt.Println(sum)
	}

}

func possible(set Set, total Set) bool {
	if set.Blue <= total.Blue && set.Green <= total.Green && set.Red <= total.Red {
		return true
	}
	return false
}

func minSet(sets []Set) (result Set) {
	for _, set := range sets {
		result.Blue = max(result.Blue, set.Blue)
		result.Green = max(result.Green, set.Green)
		result.Red = max(result.Red, set.Red)
	}
	return
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func power(set Set) int {
	return set.Blue * set.Green * set.Red
}
